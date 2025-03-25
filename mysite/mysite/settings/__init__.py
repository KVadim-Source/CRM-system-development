import os

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'mysite.settings':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings.prod'
