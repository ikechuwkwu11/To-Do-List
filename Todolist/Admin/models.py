from django.db import models
from App.models import User, Task


class Admin(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Account(models.Model):
    account = models.ForeignKey(User,on_delete=models.CASCADE)
    what_task =models.ForeignKey(Task,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)


