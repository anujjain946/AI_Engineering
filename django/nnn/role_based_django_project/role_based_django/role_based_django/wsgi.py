"""
WSGI config for role_based_django project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'role_based_django.settings')
application = get_wsgi_application()
