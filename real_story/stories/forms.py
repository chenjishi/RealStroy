# -*- coding: utf-8 -*-


from django import forms


class StoryForm(forms.Form):
    title = forms.CharField(label='', max_length=300, widget=forms.Textarea(attrs={'class': 'title_area',
                                                                                   'placeholder': '标题',
                                                                                   'rows': 1}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'content_area',
                                                                     'placeholder': '内容',
                                                                     'rows': 10}))