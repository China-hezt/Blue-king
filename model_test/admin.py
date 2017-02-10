# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Author, Book

# admin配置官方文档:  https://docs.djangoproject.com/en/1.8/ref/contrib/admin/


class AuthorAdmin(admin.ModelAdmin):
    """
    Author的Admin配置
    """
    list_display = [u'name']
    list_filter = []
    search_fields = [u'name']
    list_editable = []

    inlines = []
    filter_vertical = []
    filter_horizontal = []
    prepopulated_fields = {}
    radio_fields = {}
    readonly_fields = []
    raw_id_fields = []
    formfield_overrides = {}



class BookAdmin(admin.ModelAdmin):
    """
    Book的Admin配置
    """
    list_display = [u'name', u'author']
    list_filter = []
    search_fields = [u'name']
    list_editable = []

    inlines = []
    filter_vertical = []
    filter_horizontal = []
    prepopulated_fields = {}
    radio_fields = {}
    readonly_fields = []
    raw_id_fields = []
    formfield_overrides = {}


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
