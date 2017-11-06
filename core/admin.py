# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Log


class LogAdmin(admin.ModelAdmin):

    readonly_fields = ['id', 'uuid', 'created', 'modified']
    fields = ['user', 'endpoint', 'ip_address', 'data']
    list_display = ['id', 'endpoint', 'user', 'ip_address', 'data', 'created',
                    'modified']
    list_filter = ['endpoint']
    search_fields = ['endpoint', 'user__username', 'ip_address', 'data']


admin.site.register(Log, LogAdmin)
