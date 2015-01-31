# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acl',
            name='file',
            field=models.ForeignKey(blank=True, to='cms.File', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='acl',
            name='folder',
            field=models.ForeignKey(blank=True, to='cms.Folder', null=True),
            preserve_default=True,
        ),
    ]
