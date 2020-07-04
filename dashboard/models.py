from django.db import models

# Create your models here.
class Actions(models.Model):
    name        = models.CharField(max_length=120) #max_length required
    employee_id = models.CharField(max_length=20) #max_length required
