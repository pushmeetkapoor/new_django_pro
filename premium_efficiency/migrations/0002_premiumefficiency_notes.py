# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('premium_efficiency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='premiumefficiency',
            name='notes',
            field=models.TextField(default=b'', verbose_name=b'Notes'),
        ),
    ]
