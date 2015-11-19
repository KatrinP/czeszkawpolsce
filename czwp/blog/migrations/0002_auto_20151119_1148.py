# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='text_cz',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='post',
            name='text_pl',
            field=models.TextField(default=None),
        ),
    ]
