# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterLogo',
            fields=[
                ('ID', models.IntegerField(verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=255, default=None)),
            ],
            options={
                'db_table': 'todo_title',
            },
        ),
        migrations.AddField(
            model_name='register',
            name='title',
            field=models.CharField(verbose_name='Title', max_length=255, default=None),
        ),
        migrations.AlterField(
            model_name='register',
            name='created',
            field=models.DateTimeField(verbose_name='Date_Created', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='description',
            field=models.TextField(verbose_name='Description', default=None),
        ),
        migrations.AlterField(
            model_name='register',
            name='status',
            field=models.IntegerField(verbose_name='status', default=False),
        ),
        migrations.AlterField(
            model_name='register',
            name='task_id',
            field=models.IntegerField(verbose_name='TaskID', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='register',
            name='register_logo',
            field=models.ForeignKey(default=None, related_name='logo_text', to='TODO_app.RegisterLogo'),
        ),
    ]
