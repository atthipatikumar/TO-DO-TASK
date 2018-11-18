# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_app', '0004_auto_20181118_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='register_logo',
            field=models.ForeignKey(related_name='logo_text', to='TODO_app.RegisterLogo'),
        ),
    ]
