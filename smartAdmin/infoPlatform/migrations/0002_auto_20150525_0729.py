# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoPlatform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'm', b'\xe7\x94\xb7'), (b'f', b'\xe5\xa5\xb3')]),
            preserve_default=True,
        ),
    ]
