#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import simplejson as json

from django.shortcuts import render, render_to_response
from django.urls import reverse
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core import serializers
from detection.models import Detection

from .forms import UserForm


# Create your views here.
def index(request):
	return render(request, 'index.html', {})


@csrf_protect
def login_user(request):
	logout(request)
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('events'))

	username = password = ''
	form = UserForm(request.POST or None)
	if request.POST and str(request.POST['username']) and \
		(request.POST['password']):
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('events'))
		else:
			messages.error(request, 'Usuario o contraseña \
				incorrecta. Verifique.')

	return render(request, 'website/login.html', {'form': form})


def events(request):
	return render(request, 'website/events.html', {})


def map(request):
	detections = Detection.objects.all()
	detections_json = serializers.serialize("json", detections)
	return render(request, 'website/map.html', {'detections': detections_json})
