import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wetravel_back.settings')

app = Celery('wetravel_back')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
