from django.conf.urls import patterns, include, url
from django.contrib import admin
from smartAdmin import views
from django.views.generic import TemplateView
from infoPlatform.views import FriendListJson,UsersListJson


urlpatterns = patterns('',

   		url(r'^admin/', include(admin.site.urls)),

    	url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    	url(r'^dashboard$', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    	url(r'^userManageList$',TemplateView.as_view(template_name='userManageList.html')),
    	url(r'^myFriend$',TemplateView.as_view(template_name='friendList.html')),
	   	
	   	url(r'^usersListJson/$', UsersListJson.as_view(), name="users_list_json"),
    	url(r'^friendListJson/$', FriendListJson.as_view(), name="friend_list_json"),
)
