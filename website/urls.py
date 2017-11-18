from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from website import views as websiteviews

urlpatterns = [
	url(r'^$', websiteviews.index, name='index'),
    url(r'^login/$', websiteviews.login_user, name='login_user'),
    url(r'^events/$', websiteviews.events, name='events'),
    url(r'^map/$', websiteviews.map, name='map'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login.html'}, name='logout'),
]
