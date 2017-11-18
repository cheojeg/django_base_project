#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from django.utils.translation import ugettext as _
from django.http import HttpResponse

from .models import Agent


class AgentForm(forms.ModelForm):
    first_name = forms.CharField(label=_('Nombres'), max_length=80,
        required=True)
    middle_name = forms.CharField(label=_('Segundo Nombre'), max_length=80,
        required=False)
    last_name = forms.CharField(label=_('Apellidos'), max_length=80,
        required=True)
    middle_last_name = forms.CharField(label=_('Segundo Apellido'), 
    	max_length=80, required=False)
    agent_number = forms.CharField(label=_(unicode('Número de Agente', 
    	'utf8')), max_length=40, required=True)
    birthdate = forms.CharField(
    	label=_(unicode('Fecha de Nacimiento', 'utf8')), required=True)
    email = forms.EmailField(label=_(unicode('Correo Electrónico', 'utf8')),
        required=True)
    phone_number = forms.CharField(label=_(unicode('Teléfono', 'utf8')), 
    	max_length=20, required=True)
    sex = forms.ChoiceField(label=_('Sexo'), required=True, 
    	choices=[('F', 'Femenino'), ('M', 'Masculino')])

    class Meta:
        model = Agent
        fields = ['first_name', 'middle_name', 'last_name', 
        'middle_last_name', 'agent_number', 'birthdate', 'email', 
        'phone_number', 'sex']

    def __init__(self, *args, **kwargs):
        super(AgentForm, self).__init__(*args, **kwargs)