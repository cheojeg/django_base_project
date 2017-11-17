# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid as uuid_lib
from django.db import models
from core.models import TimeStampedModel
from django.contrib.auth.models import User


class Code(TimeStampedModel):

    uuid = models.UUIDField(primary_key=True,
                            default=uuid_lib.uuid4,
                            editable=False)
    code = models.CharField(max_length=5)
    description = models.CharField(max_length=300)

    class Meta:
        db_table = 'code'
        ordering = ['-created']

    def __str__(self):
        return self.code


class Marbete(TimeStampedModel):

    uuid = models.UUIDField(primary_key=True,
                            default=uuid_lib.uuid4,
                            editable=False)
    code_id = models.ForeignKey(Code)
    license_plate = models.CharField(max_length=25)
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    TYPE_VEHICLE = (
        ('Sedan', 'Sedan'),
        ('Camioneta', 'Camioneta'),
        ('Vehiculo de carga', 'Vehiculo de carga'),
        ('Autobus', 'Autobus'),
        ('Motocicleta', 'Motocicleta')
    )
    type_vehicle = models.CharField(max_length=150, choices=TYPE_VEHICLE)
    year_production = models.CharField(max_length=5)
    amount = models.FloatField(default=1500)
    owner = models.CharField(max_length=150)
    document_description = models.CharField(max_length=50)
    DOCUMENT_TYPES = (
        ('C', 'Cedula'),
        ('P', 'Pasaporte'),
    )
    document_type = models.CharField(max_length=40, choices=DOCUMENT_TYPES)
    oposition = models.BooleanField(default=False)
    valid = models.BooleanField(default=True)
    penalized = models.BooleanField(default=False)

    class Meta:
        db_table = 'marbete'
        ordering = ['-created']

    def __str__(self):
        return self.license_plate
