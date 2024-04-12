import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'request_queue.settings')

app = Celery('request_queue')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()