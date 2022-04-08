from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()


class Person(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()