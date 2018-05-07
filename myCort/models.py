from django.db import models

# Create your models here.

class Users(models.Model):
    Id = models.AutoField(primary_key = True)
    email = models.CharField(max_length = 30)
    name = models.CharField(max_length = 10)
    surname = models.CharField(max_length = 10)


class Reservation(models.Model):
    Id = models.AutoField(primary_key = True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.CharField(max_length = 10)
    time = models.CharField(max_length = 10)
    kort_id = models.IntegerField(default = 0)

class BlackList(models.Model):
    Id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 30)
