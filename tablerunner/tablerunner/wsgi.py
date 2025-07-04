"""WSGI config for tablerunner project."""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tablerunner.settings')

application = get_wsgi_application()
