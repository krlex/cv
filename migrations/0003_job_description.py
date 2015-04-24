# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_job_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
