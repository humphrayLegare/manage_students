#native import
import datetime

from django.db import models


# Create your models here.
class School (models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    construct_year = models.IntegerField(default=1500)

class Student (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    date = models.DateField(("Date"), default=datetime.date.today)
