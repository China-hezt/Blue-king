# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookcar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Brand', models.CharField(max_length=30)),
                ('Model', models.CharField(max_length=30)),
                ('Year', models.CharField(max_length=30)),
                ('Type', models.CharField(max_length=30)),
                ('Cooler', models.CharField(max_length=30)),
            ],
        ),
    ]
