from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255, default='Unknown')
    category = models.CharField(max_length=255, default='Public')
    deviation = models.FloatField(default=0.0)
    address = models.CharField(max_length=255, default='Public')
    region = models.CharField(max_length=255, default='Public')
    latitude = models.FloatField(default=35.68944)
    longitude = models.FloatField(default=139.69167)
    url = models.URLField(max_length=200, default='Unknown')

    def __str__(self):
        return self.name
