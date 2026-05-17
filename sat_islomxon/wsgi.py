"""
WSGI config for sat_islomxon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sat_islomxon.settings')

application = get_wsgi_application()

# Run migrations automatically on every cold start (needed for Vercel)
try:
    from django.db import connection
    from django.db.utils import OperationalError
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM auth_user LIMIT 1")
except Exception:
    from django.core.management import call_command
    call_command('migrate', '--run-syncdb', verbosity=0)
