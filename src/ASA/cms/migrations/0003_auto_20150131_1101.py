# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20150131_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='authority',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
