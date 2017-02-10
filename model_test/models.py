# -*- coding: utf-8 -*-

from django.db import models


class Author(models.Model):
    """
    Author 的 model 定义
    """
    
    name = models.CharField(verbose_name=u"姓名", max_length=32)

    class Meta:
        pass

    def __unicode__(self):
        return u'%s' % self.id


class Book(models.Model):
    """
    Book 的 model 定义
    """
    
    name = models.CharField(verbose_name=u"书名", max_length=32)
    author = models.ForeignKey(to="Author", verbose_name=u"作者")

    class Meta:
        pass

    def __unicode__(self):
        return u'%s' % self.id
