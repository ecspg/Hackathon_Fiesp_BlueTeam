# -*- coding: utf-8 -*-
try:
    from blue_backend.settings import *
except ImportError as e:
    pass

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, "static")


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
