from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from website import views as websiteviews

urlpatterns = [
	url(r'^$', websiteviews.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'website/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]