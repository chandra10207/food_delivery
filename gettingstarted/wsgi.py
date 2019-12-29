"""
WSGI config for gettingstarted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

from django.core.wsgi import get_wsgi_application
from django.conf import settings
from whitenoise import WhiteNoise


application = get_wsgi_application()

application = WhiteNoise(application, root=settings.MEDIA_ROOT, prefix='media/')
application.add_files(settings.MEDIA_ROOT, prefix='media/')


# from whitenoise.django import DjangoWhiteNoise

# application = WhiteNoise(
#     DjangoWhiteNoise(get_wsgi_application()),
#     root=settings.MEDIA_ROOT,
#     prefix='/media/',
# )

# from whitenoise import WhiteNoise

# from gettingstarted import MyWSGIApp

# application = MyWSGIApp()
# application = WhiteNoise(application, root='/path/to/static/files')
# application.add_files('/path/to/more/static/files', prefix='more-files/')
