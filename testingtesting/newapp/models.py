from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    gender = models.CharField(max_length=8)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname

class Address(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.firstname

