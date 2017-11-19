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
<<<<<<< HEAD
    url(r'^logout/$', websiteviews.logout_user, name='logout_user'),
]
=======
    url(r'^map/(?P<agent_id>.*)$', websiteviews.map, name='map'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login.html'}, name='logout'),
]
>>>>>>> 702fff08f649d9d00872cc946836cb113362f218
