#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#用户信息表
class Profile(models.Model):

	GENDER_CHOICE=(('m','男'),('f','女'))
	user=models.OneToOneField(User)
	nickName=models.CharField(max_length=50)
	department=models.CharField(max_length=50)
	gender=models.CharField(max_length=1, choices=GENDER_CHOICE)
	birthday=models.DateTimeField(auto_now_add=True)
	phoneNumber=models.CharField(max_length=11,default='00000000000')
	
	def __unicode__(self):
		return self.nickName

#好友分组信息表
class ClassInfo(models.Model):
	user=models.ForeignKey(User)
	userClassName=models.CharField(max_length=50)

	def __unicode__(self):
		return self.userClassName

#好友信息表
class FriendInfo(models.Model):

	FRIEND_STATE=(('0',"好友"),('1','陌生人'),('2','黑名'))
	user=models.ForeignKey(User,related_name='loginUser')
	userFriend=models.ForeignKey(User,related_name='user_friend')
	userClass=models.ForeignKey(ClassInfo)
	state=models.CharField(max_length=1,choices=FRIEND_STATE)
	applyTime=models.DateTimeField(auto_now_add=True)
	acceptTime=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.user.username+"---"+self.userFriend.username