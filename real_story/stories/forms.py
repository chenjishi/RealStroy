# -*- coding: utf-8 -*-


from django import forms


class StoryForm(forms.Form):
    title = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class': 'title_area'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'content_area'}))