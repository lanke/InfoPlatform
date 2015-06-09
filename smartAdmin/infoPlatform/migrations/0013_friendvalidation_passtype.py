# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoPlatform', '0012_friendvalidation'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendvalidation',
            name='passType',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'0', b'\xe6\x9c\xaa\xe5\xa4\x84\xe7\x90\x86'), (b'1', b'\xe9\x80\x9a\xe8\xbf\x87'), (b'2', b'\xe4\xb8\x8d\xe9\x80\x9a\xe8\xbf\x87')]),
            preserve_default=True,
        ),
    ]
