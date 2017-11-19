from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from website import views as websiteviews

urlpatterns = [
	url(r'^$', websiteviews.index, name='index'),
    url(r'^login/$', websiteviews.login_user, name='login_user'),
    url(r'^detection-list/$', websiteviews.detection_list, name='detection_list'),
    url(r'^logout/$', websiteviews.logout_user, name='logout_user'),
	url(r'^map/$', websiteviews.map, {'agent_id': False}, name='map'),
	url(r'^map/(?P<agent_id>.*)$', websiteviews.map, name='map'),
]
