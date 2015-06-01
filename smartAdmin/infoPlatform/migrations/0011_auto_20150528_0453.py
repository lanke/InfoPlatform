# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('infoPlatform', '0010_auto_20150528_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendinfo',
            name='user',
            field=models.ForeignKey(related_name='loginUser', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friendinfo',
            name='userFriend',
            field=models.ForeignKey(related_name='user_friend', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
