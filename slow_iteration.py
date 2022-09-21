import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'conf.settings')

import django
django.setup()
from conf.celery import app


from api.models import DailyPerformance
import time


@app.task
def daily_performance_task():
    qs = DailyPerformance.objects.filter_by_min_roi(50)[:50]
    for i in qs:
        time.sleep(60)


daily_performance_task.delay()