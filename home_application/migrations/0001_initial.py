# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipAddr', models.CharField(max_length=30)),
                ('taskName', models.CharField(max_length=30)),
                ('taskStatus', models.CharField(max_length=30)),
            ],
        ),
    ]
