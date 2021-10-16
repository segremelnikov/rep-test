from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=2, default='', blank=True)
    color = models.CharField(max_length=10)
    bordercolor = models.CharField(max_length=10, default="#000000")

    def __str__(self):
        return self.name