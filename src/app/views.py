# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import locale
import logging
import os 

from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.views import View
from django.views.generic.list import ListView
from django.utils import timezone

from sendings.settings import BASE_DIR
from . import models
from .app_settings import TIMES_SINCE_EMAIL_SEEN

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF8')

logger = logging.getLogger("django")
TRACKING_PIX_SUBPATH = "static_dev/app/pictures/email_1x1_tracking_pix.png"

# Create your views here.
class Subscribers(ListView):
    model = models.Subscriber
    paginate_by = 10
    template_name = 'app/subscribers.html'
    queryset = models.Subscriber.objects.filter(
        Q(is_staff=False) &
        Q(new_task_sending_to_emails=False) & 
        Q(when_email_message_seen__lt = datetime.now(tz=timezone.get_current_timezone()) - TIMES_SINCE_EMAIL_SEEN)
    )   

    def post(self, request, *args, **kwargs):

        data = request.POST
        subscriber_ids = data.getlist("subscribers")
        subscribers = self.queryset.filter(pk__in=subscriber_ids)
        subscribers.update(
            when_SENDING_TO_EMAILS_task_was_sent=datetime.now(tz=timezone.get_current_timezone()), 
            new_task_sending_to_emails=True
        )

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class PixelView(View):

    def get(self, request, *args, **kwargs):
        tracking_pix_data = open(os.path.join(BASE_DIR, TRACKING_PIX_SUBPATH))
        user_id = kwargs.get("user_id")
        try:
            subscriber = models.Subscriber.objects.get(pk=int(user_id))
            subscriber.when_email_message_seen = datetime.now(tz=timezone.get_current_timezone())
            subscriber.save()
            logger.info(
                u"Подписчик {first_name} {last_name} прочитал письмо.".format(
                    first_name=subscriber.first_name, 
                    last_name=subscriber.last_name
                )
            )
            
        except models.Subscriber.DoesNotExist:
            logger.warning(
                u"Подписчик с id {user_id} не был найден".format(user_id=user_id)
            )
        return HttpResponse(tracking_pix_data, content_type="image/png")