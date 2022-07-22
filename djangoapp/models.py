from statistics import mode
from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length = 500)
    def __str__(self):
        return self.title

class useradmin(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 100)
    userlogin = models.CharField(max_length = 20)
    def __str__(self):
        return self.username

class subscribers(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 60)
    phonenumber = models.CharField(max_length = 20)
    def __str__(self):
        return self.name

class comments(models.Model):
    name = models.CharField(max_length = 200)
    comment = models.CharField(max_length = 500)
    def __str__(self):
        return self.name