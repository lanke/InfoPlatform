from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Group(models.models):
	groupCode=models.CharField(max_length=8)
	groupProfile=models.TextField()
	VALI_CHOICE=(('0','不需要验证'),('1','验证'))
	needValidation=models.CharField(max_length=1,choices=VALI_CHOICE)
	rptPerson=models.ForeignKey(User)
	rptTime=models.DateTimeField(auto_now_add=True)
	delFlag=models.BooleanField()

class GroupUser(object):
	"""docstring for GroupUser"""
	group=models.ForeignKey(Group)
	user=models.ForeignKey(User)
	IS_ADMIN=(("0","否"),("1","是"))

	isAdmin=models.CharField(max_length=1,choices=IS_ADMIN)


	def __init__(self, arg):
		super(GroupUser, self).__init__()
		self.arg = arg
		
