# -*- coding: utf-8 -*-


from django import forms


class StoryForm(forms.Form):
    title = forms.CharField(label='', max_length=300, widget=forms.Textarea(attrs={'class': 'title_area',
                                                                                   'placeholder': '标题',
                                                                                   'rows': 1}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'content_area',
                                                                     'placeholder': '内容',
                                                                     'rows': 10}))


class UserForm(forms.Form):
    email = forms.EmailField(label='邮箱')
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码')