# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid as uuid_lib
from django.db import models
from core.models import TimeStampedModel
from agents.models import Agent
from dgii.models import Marbete


class Detection(TimeStampedModel):

    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(db_index=True,
                            default=uuid_lib.uuid4,
                            editable=False)
    agent_id = models.ForeignKey(Agent)
    marbete_id = models.ForeignKey(Marbete)
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.FileField(upload_to='detections')
    fined = models.NullBooleanField(default=False)

    class Meta:
        db_table = 'detection'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)
