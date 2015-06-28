from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from groupManage.models import *
# Create your views here.


def userGroupDiscuss(request):
	user = request.user
	groupIdList = GroupUser.objects.filter(user=user).values_list("group_id", flat=True)
	groupDiscussList = GroupDiscuss.objects.filter(group_id__in=groupIdList)
	paginator = Paginator(groupDiscussList, 10)
	page = request.GET.get('page')
	try:
		groupDiscussList = paginator.page(page)
	except PageNotAnInteger:
		groupDiscussList = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		groupDiscussList = paginator.page(paginator.num_pages)

	return render_to_response('groupDiscuss.html', locals(), RequestContext(request))

def group(request,groupId):
	group=Group.objects.get(pk=groupId)
	groupDiscussList=GroupDiscuss.objects.filter(group=group)
	return render_to_response('group.html', locals(), RequestContext(request))

def topic(request,topicId):
	topic=GroupDiscuss.objects.get(pk=topicId)
	replyList=ReplyDiscuss.objects.filter(groupDisscuss_id=topicId)
	return render_to_response('topic.html',locals(),RequestContext(request))
@csrf_exempt
def postReply(request,topicId):
	topic=GroupDiscuss.objects.get(pk=topicId)
	user=request.user
	if not request.POST.has_key("shtml"):
		replyList=ReplyDiscuss.objects.filter(groupDisscuss_id=topicId)
		return render_to_response('topic.html',locals(),RequestContext(request))
	if request.POST["shtml"]:
		shtml=request.POST["shtml"]
		reply=ReplyDiscuss(groupDisscuss=topic,type=1,content=shtml,replyUser=user,delFlag="0")
		reply.save()
		print reply
		replyList=ReplyDiscuss.objects.filter(groupDisscuss_id=topicId)
		return render_to_response('topic.html',locals(),RequestContext(request))
	else:
		replyList=ReplyDiscuss.objects.filter(groupDisscuss_id=topicId)
		return render_to_response('topic.html',locals(),RequestContext(request))

@csrf_exempt
def postTopic(request,groupId):
	group=Group.objects.get(pk=groupId)
	user=request.user
	if request.method=='POST':
		shtm=''
		if request.POST.has_key('shtml') and request.POST.has_key('title'):
			shtml=request.POST['shtml']
			title=request.POST['title']
			topic=GroupDiscuss(group=group,type='1',title=title,content=shtml,creatUser=user)
			topic.save()
			return render_to_response('topic.html',locals(),RequestContext(request))
	else :
		return render_to_response('postTopic.html',locals(),RequestContext(request))
