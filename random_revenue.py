import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'conf.settings')

import django
django.setup()

from api.models import DailyPerformance
import random

qs = DailyPerformance.objects.filter_by_min_roi(50)
len_qs = qs.count()
print(len_qs)
print(len_qs * 2)

revenue = 0

for index, item in enumerate(qs):
    print(str(index) + '/' + str(len_qs))
    r_num = random.uniform(0.5, 2.0)
    revenue = item.revenue * r_num
    item.revenue = revenue
    item.save()