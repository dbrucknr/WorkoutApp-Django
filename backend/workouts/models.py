from django.db import models

class Run(models.Model):
    total_time = models.DurationField()
    total_distance = models.DecimalField(decimal_places=2, max_digits=5)
    date = models.DateField()