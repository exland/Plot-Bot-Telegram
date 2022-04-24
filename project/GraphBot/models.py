from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()


class User(models.Model):
    id =  models.PositiveIntegerField( unique = True, primary_key =True)
    time_span =  models.IntegerField()
    name = models.CharField(max_length=30)
    table_num =  models.IntegerField()
    selected_num =  models.IntegerField()


class Measurement(models.Model):
    id = models.PositiveIntegerField( unique = True, primary_key =True)
    val1 = models.FloatField()
    val2 = models.FloatField()
    average = models.FloatField()
    date= models.DateField()
