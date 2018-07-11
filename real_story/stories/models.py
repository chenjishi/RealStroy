# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    summary = models.CharField(max_length=1000, default='summary for article')
    content = models.TextField(blank=True)
    category = models.CharField(max_length=10)
    author = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    image_count = models.IntegerField()
    tag = models.CharField(max_length=200)
    url = models.CharField(max_length=1000, blank=True)

    class Meta:
        db_table = 'article'
