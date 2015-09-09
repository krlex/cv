# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.AddField(
            model_name='personal',
            name='email',
            field=models.EmailField(default='krle@lugons.org', max_length=254),
            preserve_default=False,
        ),
    ]
