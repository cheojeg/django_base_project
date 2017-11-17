# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Code, Marbete


class CodeAdmin(admin.ModelAdmin):

    readonly_fields = ['uuid', 'created', 'modified']
    fields = ['code', 'description']
    list_display = ['uuid', 'code', 'description']
    search_fields = ['code', 'description']


class MarbeteAdmin(admin.ModelAdmin):

    readonly_fields = ['uuid', 'created', 'modified']
    fields = ['uuid', 'code_id', 'license_plate', 'brand', 'model',
              'type_vehicle', 'year_production', 'amount', 'owner',
              'document_description', 'document_type', 'oposition',
              'valid', 'penalized']
    list_display = ['uuid', 'code_id', 'license_plate', 'brand', 'model',
                    'amount', 'owner', 'document_description', 'document_type',
                    'oposition', 'valid', 'penalized']
    list_filter = ['oposition', 'valid', 'penalized']
    search_fields = ['license_plate', 'brand', 'model', 'document_description',
                     'owner']


admin.site.register(Marbete, MarbeteAdmin)
admin.site.register(Code, CodeAdmin)
