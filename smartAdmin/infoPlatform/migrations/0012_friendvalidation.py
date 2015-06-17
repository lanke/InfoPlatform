# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
	dependencies = [
		migrations.swappable_dependency(settings.AUTH_USER_MODEL),
		('infoPlatform', '0011_auto_20150528_0453'),
	]

	operations = [
		migrations.CreateModel(
			name='FriendValidation',
			fields=[
				('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
				('validatonInfo', models.CharField(max_length=b'200', blank=True)),
				('requestTime', models.DateTimeField(auto_now_add=True)),
				('dealTime', models.DateTimeField(auto_now=True)),
				('dealUser', models.ForeignKey(related_name='dealUser', to=settings.AUTH_USER_MODEL)),
				('requestUser', models.ForeignKey(related_name='requestUser', to=settings.AUTH_USER_MODEL)),
			],
			options={
			},
			bases=(models.Model,),
		),
	]
