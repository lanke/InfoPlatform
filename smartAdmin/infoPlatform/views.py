from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.models import User
#my models
from infoPlatform.models import ClassInfo, FriendInfo, FriendValidation


#others
from django_datatables_view.base_datatable_view import BaseDatatableView

# Create your views here.



class UsersListJson(BaseDatatableView):
	model = User
	columns = ['id', 'username', 'profile.phoneNumber', 'profile.department', 'email', 'profile.gender',
	           'profile.birthday', 'id']
	order_columns = ['id']

	def filter_queryset(self, qs):
		sSearch = self.request.GET.get('sSearch', None)
		if sSearch:
			qs = qs.filter(Q(username__istartswith=sSearch) | Q(email__istartswith=sSearch))
		return qs


class FriendListJson(BaseDatatableView):
	model = FriendInfo
	columns = ['userFriend.id', 'userFriend.username', 'userFriend.profile.phoneNumber',
	           'userFriend.profile.department', 'userFriend.email', 'userFriend.profile.gender',
	           'userFriend.profile.birthday']
	order_columns = ['id', 'username', 'email']

	def get_initial_queryset(self):
		# return queryset used as base for futher sorting/filtering
		# these are simply objects displayed in datatable
		# You should not filter data returned here by any filter values entered by user. This is because
		# we need some base queryset to count total number of records.

		user = self.request.user
		#User.objects.filter(loginUser__user=user)
		#friendList=  FriendInfo.objects.filter(user=user)

		return FriendInfo.objects.filter(user=user)

	def filter_queryset(self, qs):
		sSearch = self.request.GET.get('sSearch', None)
		if sSearch:
			qs = qs.filter(Q(username__istartswith=sSearch) | Q(email__istartswith=sSearch))
		return qs

	#nofriend user information


class UnfriendListJson(BaseDatatableView):
	model = User
	columns = ['id', 'username', 'profile.phoneNumber', 'profile.department', 'email', 'profile.gender',
	           'profile.birthday', 'id']
	order_columns = ['id', 'username', 'email']

	def get_initial_queryset(self):
		# return queryset used as base for futher sorting/filtering
		# these are simply objects displayed in datatable
		# You should not filter data returned here by any filter values entered by user. This is because
		# we need some base queryset to count total number of records.

		user = self.request.user
		#User.objects.filter(loginUser__user=user)
		#friendList=  FriendInfo.objects.filter(user=user)
		return User.objects.exclude(
			id__in=FriendInfo.objects.filter(user=user).values_list("userFriend_id", flat=True)).exclude(id=user.id)

	def filter_queryset(self, qs):
		sSearch = self.request.GET.get('sSearch', None)
		if sSearch:
			qs = qs.filter(Q(username__istartswith=sSearch) | Q(email__istartswith=sSearch))
		return qs


def Invite(request, userId):
	requestUser = request.user
	dealUser = User.objects.get(pk=userId)
	friendValidation = FriendValidation(requestUser=requestUser, dealUser=dealUser)
	friendValidation.save()
	return render_to_response('newFriend.html', locals(), RequestContext(request))


def getNotify(request):
	user = request.user
	notifyList = FriendValidation.objects.filter(dealUser=user).filter(passType="0")

	return render_to_response('notify.html', locals(), RequestContext(request))


def acceptFriendInvite(request, valiId):
	"""
	"""
	vali = FriendValidation.objects.get(pk=valiId)
	requestUser = vali.requestUser
	dealUser = vali.dealUser

	classInfo = ClassInfo.objects.get(pk=1)
	requestUserFriendInfo = FriendInfo(user=requestUser, userFriend=dealUser, userClass=classInfo, state=0)
	dealUserFriendInfo = FriendInfo(user=dealUser, userFriend=requestUser, userClass=classInfo, state=0)
	requestUserFriendInfo.save()
	dealUserFriendInfo.save()
	vali.passType = "1"
	vali.save()

	user = request.user
	notifyList = FriendValidation.objects.filter(dealUser=user).filter(passType="0")
	return render_to_response('notify.html', locals(), RequestContext(request))


def rejectFriendInvite(request, valiId):
	vali = FriendValidation.objects.get(pk=valiId)
	vali.passType = "2"
	vali.save()
	user = request.user
	notifyList = FriendValidation.objects.filter(dealUser=user).filter(passType="0")
	return render_to_response('notify.html', locals(), RequestContext(request))


