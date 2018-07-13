# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.urls import is_valid_path

from .models import Article, Tag, Story

relations = {1: ['希特勒'], 2: ['车加塞', '车祸'], 3: ['流星花园', '道明寺'], 4: ['微语录'], 5: ['段子']}


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


def bindTags(article_list):
    for article in article_list:
        aid = article.articleId
        tags = relations.get(aid)
        for t in tags:
            tag = Tag.objects.get(tag=t)
            article.tags.add(tag)
            article.save()



