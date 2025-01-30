"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import environ
from core.settings.base import BASE_DIR

env = environ.Env()
environ.Env.read_env(env_file=BASE_DIR / '.env')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('DJANGO_SETTINGS_MODULE'))

application = get_wsgi_application()
