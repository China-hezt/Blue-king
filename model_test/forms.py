# -*- coding: utf-8 -*-

from django import forms

from .models import Author, Book


class AuthorForm(forms.ModelForm):
    """
    Author的form
    """
    class Meta:
        model = Author
        fields = [u'name']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AuthorForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        
        return super(AuthorForm, self).is_valid()

    def save(self, commit=True):
        return super(AuthorForm, self).save(commit)


class BookForm(forms.ModelForm):
    """
    Book的form
    """
    class Meta:
        model = Book
        fields = [u'name', u'author']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(BookForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        
        return super(BookForm, self).is_valid()

    def save(self, commit=True):
        return super(BookForm, self).save(commit)

