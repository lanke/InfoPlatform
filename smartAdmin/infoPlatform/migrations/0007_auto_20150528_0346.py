# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
	dependencies = [
		('infoPlatform', '0006_remove_friendinfo_userfriend'),
	]

	operations = [
		migrations.AlterField(
			model_name='friendinfo',
			name='user',
			field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
			preserve_default=True,
		),
	]
