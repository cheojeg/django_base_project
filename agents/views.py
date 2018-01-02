#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
from django.template.context_processors import csrf

from .forms import AgentForm
from website.forms import UserForm
from .models import Agent
from django.contrib.auth.models import User


def profile_agent(request):
	try:
		profile_user = User.objects.create_user(
			username=request.POST['username'],
			first_name=request.POST['first_name'],
			last_name=request.POST['last_name'],
			email=request.POST['email'],
			password=request.POST['password'],
			is_superuser=False, is_active=True)
		if not profile_user:
			return False
	except Exception as err:
		return False

	return profile_user


@csrf_protect
def register_agent(request):
	form = AgentForm()
	form_user = UserForm()

	if request.method == 'POST':
		form = AgentForm(request.POST)
		formuser = UserForm(request.POST)

		if form.is_valid() and formuser.is_valid():
			user = profile_agent(request)

			if user is not None:
				form.instance.user_account_id_id = user.id
				try:
					form.save()
					messages.success(request, 'Usuario creado con éxito')
					return HttpResponseRedirect(reverse('detection_list'))
				except Exception as err:
					messages.error(request, 'Error, intente de nuevo')

	return render(request, 'agents/register.html',
		{'form': form, 'form_user' : form_user})
