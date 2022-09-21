from django.db import models
from django.db.models import Func, F

class Performance(models.Model):
    cost                = models.FloatField(default=0.0)
    revenue             = models.FloatField(default=0.0)
    created_at          = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class HourlyPerformance(Performance):
    datetime            = models.DateField()

class DailyPerformanceManager(models.QuerySet):
    def filter_by_min_roi(self, min_roi:float):
        return super().annotate(roi=(((F('revenue') - F('cost'))) / F('cost')) * 100).filter(roi__gte=min_roi)


class DailyPerformance(Performance):
    date                = models.DateField()


    objects = DailyPerformanceManager.as_manager()