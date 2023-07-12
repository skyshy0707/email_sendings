# -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging
import os

from celery import shared_task
from datetime import datetime
from django.core.mail import EmailMessage
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils import timezone

from sendings.settings import BASE_DIR, BASE_URL, EMAIL_HOST_USER
from .app_settings import DAYS_UNTIL_EMAIL_SENT
from . import models

logger = logging.getLogger("django")

@shared_task
def sending_to_emails():
    message = render_to_string(os.path.join(BASE_DIR , "templates/assets/messages/email_message.html"), { 'context': 'values' })
    now = datetime.now(tz=timezone.get_current_timezone())
    subscribers = models.Subscriber.objects.filter(
        Q(new_task_sending_to_emails=True) &
        Q(when_SENDING_TO_EMAILS_task_was_sent__lt = now - DAYS_UNTIL_EMAIL_SENT)
    )

    for subscriber in subscribers:
        first_name = subscriber.first_name
        last_name = subscriber.last_name

        html_message = message.format(
            first_name=first_name,
            last_name=last_name,
            base_url=BASE_URL,
            user_id=subscriber.id
        )

        sender = EmailMessage(
            subject="Предложение пройти мед. обследование",
            body=html_message,
            from_email=EMAIL_HOST_USER,
            to=[subscriber.email],
        )

        sender.content_subtype = "html"
        connection = sender.send()
        if not connection:
            logger.warning(
                u"Пользователю {username}: {first_name} {last_name} не"\
                u" было доставлено сообщение, поскольку он не указан email".format(
                    first_name=first_name, last_name=last_name, username=subscriber.username
                )
            )
        else:
            subscriber.new_task_sending_to_emails = False
            subscriber.save()

    return "Done"