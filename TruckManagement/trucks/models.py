from django.db import models

class Trucks(models.Model):
    truck_model = models.CharField(max_length=255)
    year_release = models.CharField(max_length=255)
    gearbox_model = models.CharField(max_length=255)
    engine_model = models.CharField(max_length=255)
    chassis_type = models.CharField(max_length=255)
