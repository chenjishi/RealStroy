# -*- coding: utf-8 -*-


from django import forms
from django.core.exceptions import ValidationError

from models import User


class StoryForm(forms.Form):
    title = forms.CharField(label='', max_length=300, widget=forms.Textarea(attrs={'class': 'title_area',
                                                                                   'placeholder': '标题',
                                                                                   'rows': 1}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'content_area',
                                                                     'placeholder': '内容',
                                                                     'rows': 10}))


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='邮箱', max_length=150)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        try:
            User.objects.get(email=email)
            return email
        except User.DoesNotExist:
            raise ValidationError('用户未注册')


class CustomUserCreationForm(forms.Form):
    email = forms.EmailField(label='邮箱', max_length=150)
    username = forms.CharField(label='用户名', max_length=150)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError('用户名已注册')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError('邮箱已被注册')
        return email

    def clean_password(self):
        pwd = self.cleaned_data['password']
        if len(pwd) < 6:
            raise ValidationError('密码需要大于6位')
        return pwd

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['username'],
            self.cleaned_data['password'])

        return user
