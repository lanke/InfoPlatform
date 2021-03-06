#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
	"""用户信息"""
	GENDER_CHOICE = (('m', '男'), ('f', '女'))
	user = models.OneToOneField(User)
	nickName = models.CharField(max_length=50)
	department = models.CharField(max_length=50)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
	birthday = models.DateTimeField(auto_now_add=True)
	phoneNumber = models.CharField(max_length=11, default='00000000000')

	def __unicode__(self):
		return self.nickName


class ClassInfo(models.Model):
	"""好友分组信息表"""
	user = models.ForeignKey(User)
	userClassName = models.CharField(max_length=50)

	def __unicode__(self):
		return self.userClassName


class FriendInfo(models.Model):
	"""好友信息表"""
	FRIEND_STATE = (('0', "好友"), ('1', '陌生人'), ('2', '黑名'))
	user = models.ForeignKey(User, related_name='loginUser')
	userFriend = models.ForeignKey(User, related_name='user_friend')
	userClass = models.ForeignKey(ClassInfo)
	state = models.CharField(max_length=1, choices=FRIEND_STATE)
	applyTime = models.DateTimeField(auto_now_add=True)
	acceptTime = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.user.username + "---" + self.userFriend.username


class FriendValidation(models.Model):
	"""好友验证消息"""
	PASS_TYPE_STATE = (('0', "未处理"), ('1', '通过'), ('2', '不通过'))
	requestUser = models.ForeignKey(User, related_name='requestUser')
	dealUser = models.ForeignKey(User, related_name='dealUser')
	validatonInfo = models.CharField(max_length="200", blank=True)
	requestTime = models.DateTimeField(auto_now_add=True)
	dealTime = models.DateTimeField(auto_now=True)
	passType = models.CharField(max_length=1, choices=PASS_TYPE_STATE, default="0")

	def __unicode__(self):
		return self.requestUser.username + "---" + self.dealUser.username






