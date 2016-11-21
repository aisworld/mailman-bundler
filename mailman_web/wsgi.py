"""
WSGI config for mailman-web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

# Set the DJANGO_SETTINGS_MODULE environnement variable to the python path to
# your settings module (testing or production)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
