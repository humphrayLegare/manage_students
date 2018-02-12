#native import
import datetime

from django.db import models


# Create your models here.
class School (models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    construct_year = models.IntegerField(default=1500)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Field(models.Model):
    name = models.CharField(max_length=60)

class Program(models.Model):
    name = models.CharField(max_length=60)

    #foreign key
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

class Sex(models.Model):
    name = models.CharField(max_length=20)


class Student (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    city = models.CharField(max_length=30)
    birth_date = models.DateField(("Date"), default=datetime.date.today)

    #foreign key
    sex = models.ForeignKey(Sex, default="male", on_delete=models.CASCADE)
    program = models.ForeignKey(Program, default=0, on_delete=models.CASCADE)






