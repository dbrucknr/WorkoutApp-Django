from django.db import models

class Run(models.Model):
    total_time = models.DurationField()
    total_distance = models.DecimalField(decimal_places=2, max_digits=5)
    # _average_mile = None
    date = models.DateField()

    # @property
    # def calculate_avg_mile(self):
    #     if self._average_mile is None:
    #         self._average_mile = self.total_time/self.total_distance
    #         print(self._average_mile)
    #     return self._average_mile