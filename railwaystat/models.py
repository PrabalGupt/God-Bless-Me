from django.db import models

# Create your models here.
class TrainStatus(models.Model):
    TrainName = models.CharField(max_length=1000)
    Destination = models.CharField(max_length=100)

class UserDetails(models.Model):
    Username = models.CharField(max_length=100)
    Age = models.CharField(max_length=3)
    password = models.CharField(max_length=100)