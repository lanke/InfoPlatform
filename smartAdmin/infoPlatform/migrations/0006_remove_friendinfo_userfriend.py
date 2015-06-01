# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoPlatform', '0005_auto_20150528_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendinfo',
            name='userFriend',
        ),
    ]
