# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
	dependencies = [
		migrations.swappable_dependency(settings.AUTH_USER_MODEL),
		('infoPlatform', '0003_profile_phonenumber'),
	]

	operations = [
		migrations.CreateModel(
			name='ClassInfo',
			fields=[
				('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
				('userClassName', models.CharField(max_length=50)),
				('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
			],
			options={
			},
			bases=(models.Model,),
		),
		migrations.CreateModel(
			name='FriendInfo',
			fields=[
				('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
				('state', models.CharField(max_length=1, choices=[(b'0', b'\xe5\xa5\xbd\xe5\x8f\x8b'),
				                                                  (b'1', b'\xe9\x99\x8c\xe7\x94\x9f\xe4\xba\xba'),
				                                                  (b'2', b'\xe9\xbb\x91\xe5\x90\x8d')])),
				('applyTime', models.DateTimeField(auto_now_add=True)),
				('acceptTime', models.DateTimeField(auto_now_add=True)),
				('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
				('userClass', models.ForeignKey(to='infoPlatform.ClassInfo')),
				('userFriend', models.ForeignKey(related_name='user_friend', to=settings.AUTH_USER_MODEL)),
			],
			options={
			},
			bases=(models.Model,),
		),
	]
