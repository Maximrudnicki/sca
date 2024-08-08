from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=255)
    experience = models.IntegerField()
    breed = models.CharField(max_length=255)
    salary = models.IntegerField()
