# -*- coding: utf-8 -*-

from django.db import models

class Bookcar(models.Model):
    Brand = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    Year = models.CharField(max_length=30)
    Type = models.CharField(max_length=30)
    Cooler = models.CharField(max_length=30)

    def __unicode__(self):
        return self.Brand


class Bookcelery(models.Model):
    Brand = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    Year = models.CharField(max_length=30)
    Type = models.CharField(max_length=30)
    Cooler = models.CharField(max_length=30)

    def __unicode__(self):
        return self.Brand
