from django.contrib import admin
from groupManage.models import *

# Register your models here.
admin.site.register(Group)
admin.site.register(GroupUser)
admin.site.register(GroupDiscuss)
admin.site.register(ReplyDiscuss)
admin.site.register(GroupNotice)
