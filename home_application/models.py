# -*- coding: utf-8 -*-

from django.db import models

class Ping(models.Model):
    ipAddr = models.CharField(max_length=30)
    taskName = models.CharField(max_length=30)
    taskStatus = models.CharField(max_length=30)
