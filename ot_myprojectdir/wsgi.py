"""
WSGI config for ot_myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "ot_myproject.settings")
dotenv_path = os.path.join(
                      os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
