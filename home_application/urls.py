# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('home_application.views',
    (r'^$', 'home'),
    (r'^excute_task', 'execute_task'),
)
