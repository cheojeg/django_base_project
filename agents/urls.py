from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from agents import views as agentviews

urlpatterns = [
    url(r'^register-agent/$', agentviews.register_agent, name='register_agent'),
]
