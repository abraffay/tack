# from __future__ import absolute_import
import os
from celery import Celery
# from celery.schedules import crontab
# from datetime import datetime ,timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('conf')
app.conf.update(
    CELERY_TIMEZONE =  'Asia/Karachi'
)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()