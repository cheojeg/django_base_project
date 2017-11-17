# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid as uuid_lib
from django.db import models
from core.models import TimeStampedModel
from django.contrib.auth.models import User


class Agent(TimeStampedModel):

    uuid = models.UUIDField(primary_key=True,
                            default=uuid_lib.uuid4,
                            editable=False)
    user_account_id = models.ForeignKey(User)
    agent_number = models.CharField(max_length=40)
    first_name = models.CharField(max_length=80)
    middle_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    middle_last_name = models.CharField(max_length=80)
    birthdate = models.DateField()
    SEX = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    sex = models.CharField(max_length=1, choices=SEX)
    email = models.EmailField(default='')
    phone_number = models.CharField(max_length=20, default='')

    class Meta:
        db_table = 'agent'
        ordering = ['-created']

    def __str__(self):
        return self.first_name + ' ' + self.last_name
