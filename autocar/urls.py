# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('autocar.views',
    (r'^$', 'index'),
    (r'^index', 'index'),
    (r'^table1_1', 'table1_1'),
    (r'^table.html$', 'table'),
    (r'^table_1', 'table'),
    (r'^table1', 'table1'),
    (r'^table2', 'table2'),
)
