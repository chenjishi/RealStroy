# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader

from .models import Article, Story


def index(request):
    print request.path
    article_list = Article.objects.order_by('pub_date').all()
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