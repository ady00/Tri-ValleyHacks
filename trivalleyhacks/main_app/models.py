from django.db import models

class Painting(models.Model):
    title = models.CharField(max_length = 100)
    time_period = models.CharField(max_length = 80)
    location = models.CharField(max_length = 80)
    artist = models.CharField(max_length = 80)


