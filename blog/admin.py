# -*- coding:utf-8 -*-
"""
__title__ = ""
__author__ = "chengj"
__mtime__ = "16-8-26"
"""

from django.contrib import admin
from models import Publisher, Book, Auther

class AutherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publish_date')
    list_filter = ('publish_date',)
    date_hierarchy = 'publish_date'
    filter_horizontal = ('authers',)
    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Auther, AutherAdmin)