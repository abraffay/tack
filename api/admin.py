from django.contrib import admin
from api.models import HourlyPerformance, DailyPerformance

admin.site.register(DailyPerformance)
admin.site.register(HourlyPerformance)