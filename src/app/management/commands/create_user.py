# -*- coding: utf-8 -*-
import locale
import logging

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF8')

DEFAULT_PASSWORD = "qwerty123456"
logger = logging.getLogger("django")

class Command(BaseCommand):

    help = u"Создаёт пользователя"

    def add_arguments(self, parser):
        parser.add_argument("username", type=str)
        parser.add_argument("--email", type=str)
        parser.add_argument("--password", type=str, default=DEFAULT_PASSWORD)
        parser.add_argument("--first_name", type=str, default="")
        parser.add_argument("--last_name", type=str, default="")

    def handle(self, *args, **kwargs):

        user = get_user_model()
        username = kwargs.get("username")
        email = kwargs.get("email")
        password = kwargs.get("password")
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")

        instance = user(
            username=username, 
            email=email, 
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        try:
            instance.clean_fields()
            user.objects.create_user(
            username=username, 
            email=email, 
            password=password,
            first_name=first_name,
            last_name=last_name,
        )   
        except ValidationError:
            logger.warning(
                u"Пользователь не создан.\
                Параметры полей username={username}, email={email},\
                password={password}, first_name={first_name}\
                last_name={last_name} не корректны".format(
                    username=username, 
                    email=email, 
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )
            )
        except IntegrityError:
            logger.warning(u"Пользователь с таким {username} существует".format(username=username))