# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid as uuid_lib
from django.db import models
from core.models import TimeStampedModel
from agents.models import Agent
from dgii.models import Marbete


class DetectionManager(models.Manager):

    def create_detection(self, data):
        # fugitive = None
        # fbi_list_id = FBIList.objects.filter(description=data['fbi_list_id'])
        # check_fugitive = Fugitives.objects.filter(
        #     detail_url=data['detail_url'])
        try:
            # if fbi_list_id.exists() and not check_fugitive.exists():
            detection = self.create(
                agent_id=data['agent_id'],
                marbete_id=data['marbete_id'],
                latitude=data['latitude'],
                longitude=data['longitude']
            )
        except IntegrityError:
            print "Error de integridad BD!!!!"
        finally:
            return detection


class Detection(TimeStampedModel):

    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(db_index=True,
                            default=uuid_lib.uuid4,
                            editable=False)
    agent_id = models.ForeignKey(Agent)
    marbete_id = models.ForeignKey(Marbete)
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.FileField(upload_to='detections', blank=True, null=True)
    fined = models.NullBooleanField(default=False)
    objects = DetectionManager()

    class Meta:
        db_table = 'detection'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)