# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoPlatform', '0002_auto_20150525_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(default=b'00000000000', max_length=11),
            preserve_default=True,
        ),
    ]
