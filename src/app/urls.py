# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Subscribers.as_view()),
    url(r'^tracking/(?P<user_id>[0-9]+)/$', views.PixelView.as_view()),
]