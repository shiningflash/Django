from django.contrib.gis.db import models

class Hospital(models.Model):
    # latitude = models.FloatField()
    # longitude = models.FloatField()
    location = models.PointField(null=True)
    name = models.CharField(max_length=255, unique=True)
    active_status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    