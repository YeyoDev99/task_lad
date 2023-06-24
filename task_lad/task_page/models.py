from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.contrib import admin
from django.utils import timezone



class User(AbstractUser):
    name = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(default='default.jpg', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=timezone.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    completion = models.BooleanField(default=False)
    delay = models.BooleanField(default=False)
    completed = models.DateTimeField(null=True, blank=True)

    @admin.display(boolean=True, ordering="completion", description="completed?")
    def completion_validation(self):
        return self.completion
    

    @admin.display(boolean=True, ordering="deadline", description="delayed completion?")
    def delay_validation(self):
        return self.delay


    def __str__(self):
        return self.title




