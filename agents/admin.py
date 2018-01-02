# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Agent


class AgentAdmin(admin.ModelAdmin):

    readonly_fields = ['uuid', 'created', 'modified']
    fields = ['user_account_id', 'agent_number', 'first_name', 'middle_name',
              'last_name', 'middle_last_name', 'birthdate', 'sex', 'email',
              'phone_number']
    list_display = ['user_account_id', 'agent_number', 'first_name',
                    'middle_name', 'last_name', 'middle_last_name',
                    'birthdate', 'sex', 'email', 'phone_number', 'created',
                    'modified']
    list_filter = ['sex']
    search_fields = ['agent_number', 'user_account_id__username', 'first_name',
                     'middle_name', 'last_name', 'middle_last_name', 'email',
                     'phone_number']


admin.site.register(Agent, AgentAdmin)
