from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from groupManage.views import userGroupDiscuss,group,topic,postReply,postTopic
urlpatterns = patterns('',

    	url(r'^groupList$', TemplateView.as_view(template_name='userManageList.html')),
        url(r'^$', userGroupDiscuss,name='userGroupDiscuss'),
        url(r'^(?P<groupId>\d+)$', group,name='group'),
        url(r'^topic/(?P<topicId>\d+)$', topic,name='topic'),
        url(r'^postReply/(?P<topicId>\d+)$', postReply,name='postReply'),
        url(r'^postTopic/(?P<groupId>\d+)$', postTopic,name='postTopic'),
)