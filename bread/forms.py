# coding: utf-8

from __future__ import unicode_literals

from django import forms

from bread.models import Bread, Bread_object


class BreadEditForm(forms.ModelForm):
    class Meta:
        model = Bread
        exclude = ('filtered_image_file', 'release_at',)

class BreadObjectEditForm(forms.ModelForm):
    class Meta:
        model = Bread_object
        exclude = ('filtered_image_file',)