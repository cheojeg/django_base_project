#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from django.utils.translation import ugettext as _
from django.http import HttpResponse

from .models import User


msg_required = 'Este campo es requerido.'


class UserForm(forms.ModelForm):
    username = forms.CharField(label=_(unicode('Nombre de Usuario', 'utf8')),
        max_length=150, required=True)
    password = forms.CharField(label=_(unicode('Contraseña', 'utf8')),
        max_length=128, required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['password', 'username']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
