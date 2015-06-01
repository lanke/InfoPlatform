from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
#my models
from infoPlatform.models import ClassInfo,FriendInfo


#others
from django_datatables_view.base_datatable_view import BaseDatatableView

# Create your views here.



class UsersListJson(BaseDatatableView):
    model = User
    columns = ['id', 'username','profile.phoneNumber','profile.department','email','profile.gender','profile.birthday']
    order_columns = ['id']
    
    def filter_queryset(self, qs):
        sSearch = self.request.GET.get('sSearch', None)
        if sSearch:
            qs = qs.filter(Q(username__istartswith=sSearch) | Q(email__istartswith=sSearch))
        return qs




class FriendListJson(BaseDatatableView):
    model = FriendInfo
    columns = ['userFriend.id', 'userFriend.username','userFriend.profile.phoneNumber','userFriend.profile.department','userFriend.email','userFriend.profile.gender','userFriend.profile.birthday']
    order_columns = ['id','username', 'email']
    
    def get_initial_queryset(self):
        # return queryset used as base for futher sorting/filtering
        # these are simply objects displayed in datatable
        # You should not filter data returned here by any filter values entered by user. This is because
        # we need some base queryset to count total number of records.

        user=self.request.user
        #User.objects.filter(loginUser__user=user)
        #friendList=  FriendInfo.objects.filter(user=user)

        return FriendInfo.objects.filter(user=user)
    def filter_queryset(self, qs):
        sSearch = self.request.GET.get('sSearch', None)
        if sSearch:
            qs = qs.filter(Q(username__istartswith=sSearch) | Q(email__istartswith=sSearch))
        return qs





