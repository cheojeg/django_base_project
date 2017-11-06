# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid as uuid_lib
from django.db import models
from django.db import IntegrityError
from django.contrib.auth.models import User
import logging


class TimeStampedModel(models.Model):
    """
    An abstract model just for provide created and modified dates
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LogManager(models.Manager):

    def create_log_record(self, endpoint, request):
        from core.models import Log
        log = None
        try:
            log = self.create(
                endpoint=endpoint,
                user=request.user,
                ip_address=request._request.environ['REMOTE_ADDR'],
                data=str(request.query_params)
            )
        except Exception:
            logger = logging.getLogger('base_project.log')
            logger.error('LOG - LogManager: Something is wrong saving '
                         'records on log request')
        finally:
            return log


class Log(TimeStampedModel):

    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False)
    endpoint = models.CharField(max_length=80, default='')
    user = models.ForeignKey(User, default=None)
    ip_address = models.GenericIPAddressField(protocol='both')
    data = models.TextField(default='', blank=True, null=True)
    objects = LogManager()

    class Meta:
        db_table = 'log'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)
