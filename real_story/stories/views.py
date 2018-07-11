# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader

from .models import Article


def index(request):
    article_list = Article.objects.order_by('pub_date').all()
    template = loader.get_template('stories/index.html')
    context = {'article_list': article_list}

    return HttpResponse(template.render(context, request))



