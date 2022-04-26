from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User_signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=15, null=True)
    company = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    name = models.CharField(max_length=120)
    Roll_num = models.IntegerField()
    city = models.CharField(max_length=20)
