# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

DEFAULT_DATE_VALUE = datetime(year=2000, month=1, day=1, tzinfo=timezone.get_current_timezone())
# Create your models here.

class Subscriber(AbstractUser):

    new_task_sending_to_emails = models.BooleanField(verbose_name="Статус нового задания по отправке сообщения", default=False)
    when_email_message_seen = models.DateTimeField(verbose_name="Дата просмотра сообщения", default=DEFAULT_DATE_VALUE)
    when_SENDING_TO_EMAILS_task_was_sent = models.DateTimeField(verbose_name="Дата отправки задания по доставке email", default=DEFAULT_DATE_VALUE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    class Meta:
        ordering = ("id",)