from django.db import models
from django.contrib.auth.models import User
from addpeople.models import Item
from estpeople.models import Page

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    q = models.CharField(max_length=300, default='', blank=True)
    a = models.CharField(max_length=3000, default='', blank=True)
