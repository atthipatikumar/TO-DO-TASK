# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_app', '0002_auto_20181118_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='register_logo',
            field=models.ForeignKey(related_name='logo_text', to='TODO_app.RegisterLogo'),
        ),
        migrations.AlterField(
            model_name='register',
            name='status',
            field=models.IntegerField(verbose_name='status', primary_key=True, default=False),
        ),
        migrations.AlterUniqueTogether(
            name='register',
            unique_together=set([('task_id', 'description', 'register_logo')]),
        ),
        migrations.AlterUniqueTogether(
            name='registerlogo',
            unique_together=set([('title',)]),
        ),
    ]
