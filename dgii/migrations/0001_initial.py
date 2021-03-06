# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 03:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('code', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['-created'],
                'db_table': 'code',
            },
        ),
        migrations.CreateModel(
            name='Marbete',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('license_plate', models.CharField(max_length=25, unique=True)),
                ('brand', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('type_vehicle', models.CharField(choices=[('Sedan', 'Sedan'), ('Camioneta', 'Camioneta'), ('Vehiculo de carga', 'Vehiculo de carga'), ('Autobus', 'Autobus'), ('Motocicleta', 'Motocicleta')], max_length=150)),
                ('year_production', models.CharField(max_length=5)),
                ('amount', models.FloatField(default=1500)),
                ('owner', models.CharField(max_length=150)),
                ('document_description', models.CharField(max_length=50)),
                ('document_type', models.CharField(choices=[('C', 'Cedula'), ('P', 'Pasaporte')], max_length=40)),
                ('oposition', models.BooleanField(default=False)),
                ('valid', models.BooleanField(default=True)),
                ('penalized', models.BooleanField(default=False)),
                ('code', models.ForeignKey(db_column='code_id', default=None, on_delete=django.db.models.deletion.CASCADE, to='dgii.Code')),
            ],
            options={
                'ordering': ['-created'],
                'db_table': 'marbete',
            },
        ),
    ]
