# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_auto_20150510_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='status',
            field=models.CharField(default=b'b', max_length=1, choices=[(b'd', b'Diamond'), (b'p', b'Platinum'), (b'g', b'Gold'), (b's', b'Silver'), (b'b', b'Bronze')]),
        ),
    ]
