# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.model_list, name='model_test_model_list'),
]

# Author的urls映射.
# 注意: 如果增加url配置, 其name的值不能重复(全局唯一)! 否则可能导致页面上某些跳转错误
urlpatterns += [
    url(r'^author/$', views.author_list, name='model_test_author_list'),
    url(r'^author/create/$', views.author_create, name='model_test_author_create'),
    url(r'^author/delete/(?P<id>[-\w]+)/$', views.author_delete, name='model_test_author_delete'),
    url(r'^author/update/(?P<id>[-\w]+)/$', views.author_update, name='model_test_author_update'),
    url(r'^author/(?P<id>[-\w]+)/$', views.author_detail, name='model_test_author_detail'),
]

# Book的urls映射.
# 注意: 如果增加url配置, 其name的值不能重复(全局唯一)! 否则可能导致页面上某些跳转错误
urlpatterns += [
    url(r'^book/$', views.book_list, name='model_test_book_list'),
    url(r'^book/create/$', views.book_create, name='model_test_book_create'),
    url(r'^book/delete/(?P<id>[-\w]+)/$', views.book_delete, name='model_test_book_delete'),
    url(r'^book/update/(?P<id>[-\w]+)/$', views.book_update, name='model_test_book_update'),
    url(r'^book/(?P<id>[-\w]+)/$', views.book_detail, name='model_test_book_detail'),
]



