# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Story(models.Model):
    storyId = models.AutoField(primary_key=True)
    content = models.TextField()

    def __str__(self):
        if not self.content:
            return 'empty'
        else:
            if len(self.content) <= 30:
                return self.content
            else:
                return self.content[:30]

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


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(verbose_name='username', max_length=150, default='username')
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'user'




