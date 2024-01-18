"""
WSGI config for character_guessing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append('/Users/work/PycharmProjects/Quiz+Project/character_guessing')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'character_guessing.settings')

application = get_wsgi_application()
