# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from django.contrib import admin
from .models import Tag, Article, Story, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    list_display = ('email', 'is_staff')


admin.site.register(User, UserAdmin)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Story)
