# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_app', '0003_auto_20181118_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='register_logo',
            field=models.ForeignKey(primary_key=True, unique=True, related_name='logo_text', to='TODO_app.RegisterLogo'),
        ),
        migrations.AlterField(
            model_name='register',
            name='status',
            field=models.CharField(verbose_name='status', max_length=255, default=False),
        ),
        migrations.AlterUniqueTogether(
            name='register',
            unique_together=set([('task_id', 'register_logo')]),
        ),
    ]
