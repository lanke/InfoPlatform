# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('infoPlatform', '0004_classinfo_friendinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendinfo',
            name='user',
            field=models.ForeignKey(related_name='friendInfo', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
