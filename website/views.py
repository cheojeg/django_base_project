# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
	return render(request, 'index.html', {})


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            # Return a 'disabled account' error message
            messages.error(request, _(unicode('Correo Electrónico o \
                contraseña incorrecta. Verifique.', 'utf8')))
    else:
        # Return an 'invalid login' error message.
        messages.error(request, _(unicode('Correo Electrónico o \
                contraseña incorrecta. Verifique.', 'utf8')))
    return True