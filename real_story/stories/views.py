# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .models import Article, Story, User, UserManager
from .forms import StoryForm, CustomUserCreationForm, UserLoginForm
from datetime import datetime
from django.shortcuts import render
from django.core.exceptions import ValidationError


def index(request):
    username = ''
    if request.user.is_authenticated:
        username = request.user.username

    article_list = Article.objects.all()
    template = loader.get_template('stories/index.html')
    context = {'article_list': article_list,
               'username': username}

    return HttpResponse(template.render(context, request))


def tag(request, tag_id):
    article_list = Article.objects.order_by('pub_date').filter(tags__tagId=tag_id)
    template = loader.get_template('stories/index.html')
    context = {'article_list': article_list}
    return HttpResponse(template.render(context, request))


def post(request, article_id):
    article = Article.objects.get(articleId=article_id)
    story = Story.objects.get(storyId=article.content_id)
    template = loader.get_template('stories/story.html')
    context = {'article': article, 'story': story}
    return HttpResponse(template.render(context, request))


def submit(request):
    template = loader.get_template('stories/submit.html')
    context = {'form': StoryForm()}

    return HttpResponse(template.render(context, request))


def create_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = Story()
            story.content = form.cleaned_data['content']
            story.save()

            a = Article()
            a.title = form.cleaned_data['title']
            a.content = story
            a.summary = story.content[:60]
            a.pub_date = datetime.now()
            a.image_count = 0

            a.save()

    article_list = Article.objects.order_by('pub_date').all()
    template = loader.get_template('stories/index.html')
    context = {'article_list': article_list}

    return HttpResponse(template.render(context, request))


def login_in(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            print 'user', user
            if user is not None:
                login(request, user)
                return redirect('/stories/')
            else:
                return render(request, 'stories/login.html', {'form': form, 'errorMsg': '密码错误!'})
    else:
        if request.user.is_authenticated:
            logout(request)
            return redirect('/stories/')
        else:
            form = UserLoginForm()

    return render(request, 'stories/login.html', {'form': form, 'login': False})


def sign_in(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return redirect('/stories/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'stories/sign_in.html', {'form': form, 'login': False})
