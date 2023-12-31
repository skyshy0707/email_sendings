# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sendings.settings')

app = Celery('sendings')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sending_to_emails': {
        'task': 'app.tasks.sending_to_emails',
        'schedule': crontab(minute=0, hour=20)
    },
}