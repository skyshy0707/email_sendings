# -*- coding: utf-8 -*-
import os

def env_variables(request):
    return {
        'BASE_URL': os.environ['BASE_URL'],
        'EMAIL_HOST_USER': os.environ['EMAIL_HOST_USER'],
        'EMAIL_HOST_PASSWORD': os.environ['EMAIL_HOST_PASSWORD']
    }