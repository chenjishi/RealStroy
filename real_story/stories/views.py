# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Article, Story
from .forms import StoryForm
from datetime import datetime


def index(request):
    article_list = Article.objects.all()
    template = loader.get_template('stories/index.html')
    context = {'article_list': article_list}

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


