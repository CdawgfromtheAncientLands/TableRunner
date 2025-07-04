"""ASGI config for tablerunner project."""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tablerunner.settings')

application = get_asgi_application()
