# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Story(models.Model):
    storyId = models.AutoField(primary_key=True)
    content = models.TextField()

    class Meta:
        db_table = 'story'


class Tag(models.Model):
    tagId = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return unicode(self.tag)


class Article(models.Model):
    articleId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)
    content = models.OneToOneField(Story, on_delete=models.CASCADE)
    category = models.CharField(max_length=10)
    author = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    image_count = models.IntegerField()
    url = models.CharField(max_length=1000, blank=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        db_table = 'article'

    def __str__(self):
        return self.title


