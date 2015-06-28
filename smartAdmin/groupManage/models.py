#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Group(models.Model):
	"""111"""
	groupCode = models.CharField(max_length=8)
	groupName=models.CharField(max_length=20)
	groupProfile = models.TextField()
	VALI_CHOICE = (('0', '不需要验证'), ('1', '验证'))
	needValidation = models.CharField(max_length=1, choices=VALI_CHOICE)
	rptPerson = models.ForeignKey(User)
	rptTime = models.DateTimeField(auto_now_add=True)
	delFlag = models.BooleanField(default=True)
	def __unicode__(self):
		return self.groupName + "---" + self.groupCode

class GroupUser(models.Model):
	"""群组用户"""
	group = models.ForeignKey(Group)
	user = models.ForeignKey(User)
	IS_ADMIN = (("0", "否"), ("1", "是"))

	isAdmin = models.CharField(max_length=1, choices=IS_ADMIN)
	def __unicode__(self):
		return self.group.groupName + "---" + self.user.username

class GroupDiscuss(models.Model):
	"""群组讨论"""
	group = models.ForeignKey(Group)
	type = models.CharField(max_length=1)
	title = models.CharField(max_length=200)
	content = models.TextField()
	browseCount = models.IntegerField(default=0)
	replyCount = models.IntegerField(default=0)
	creatUser = models.ForeignKey(User)
	creatTime = models.DateTimeField(auto_now_add=True)
	lockFlag = models.BooleanField(default=True)
	delFlag = models.BooleanField(default=True)
	def __unicode__(self):
		return self.group.groupName + "---" + self.title

class ReplyDiscuss(models.Model):
	"""群组讨论回复"""
	groupDisscuss = models.ForeignKey(GroupDiscuss)
	type = models.CharField(max_length=1)
	content = models.TextField()
	replyUser = models.ForeignKey(User)
	replyTime = models.DateTimeField(auto_now_add=True)
	delFlag = models.BooleanField(default=True)
	def __unicode__(self):
		return self.groupDisscuss.title + "---" + self.replyUser.username

class GroupNotice(models.Model):
	"""群公告"""
	gorup = models.ForeignKey(Group)
	content = models.CharField(max_length=200)
	topFlag = models.BooleanField(default=True)
	createUser = models.ForeignKey(User)
	createTime = models.DateTimeField(auto_now_add=True)
	delFlag = models.BooleanField(default=True)
	def __unicode__(self):
		return self.group.groupName + "---" + self.content

