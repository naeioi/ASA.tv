# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACL',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('r', models.BooleanField(default=False)),
                ('w', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('size', models.BigIntegerField()),
                ('filehash', models.CharField(unique=True, max_length=64)),
                ('filename', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('path', models.CharField(unique=True, max_length=128)),
                ('file', models.ManyToManyField(blank=True, related_name='folder', to='cms.File', db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nick_name', models.CharField(max_length=128)),
                ('passwd', models.CharField(max_length=128)),
                ('register_at', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('authority', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to='cms.User', db_index=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='folder',
            name='host',
            field=models.ManyToManyField(blank=True, related_name='host', to='cms.User', db_index=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='folder',
            name='parent_folder',
            field=models.ForeignKey(related_name='folder', null=True, blank=True, to='cms.Folder'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='folder',
            name='super_host',
            field=models.ManyToManyField(blank=True, related_name='super_host', to='cms.User', db_index=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acl',
            name='folder',
            field=models.ForeignKey(to='cms.Folder'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acl',
            name='user',
            field=models.ForeignKey(to='cms.User'),
            preserve_default=True,
        ),
    ]
