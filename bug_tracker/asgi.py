"""
ASGI config for bug_tracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.production')

if settings.DEBUG:
    application = StaticFilesHandler(get_asgi_application())
else:
    application = get_asgi_application()
