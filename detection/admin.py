# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Detection


class DetectionAdmin(admin.ModelAdmin):

    readonly_fields = ['id', 'uuid', 'created', 'modified']
    fields = ['id', 'uuid', 'agent_id', 'marbete_id', 'latitude', 'longitude',
              'photo', 'fined']
    list_display = ['id', 'uuid', 'agent_id', 'marbete_id', 'latitude',
                    'longitude', 'photo', 'fined', 'created', 'modified']
    list_filter = ['fined', 'agent_id']
    search_fields = ['marbete_id__license_plate', 'agent_id__first_name',
                     'agent_id__last_name']


admin.site.register(Detection, DetectionAdmin)
