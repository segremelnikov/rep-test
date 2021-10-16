from django.db import models
from django.contrib.auth.models import User
from addpeople.models import Item
from estpeople.models import Page

class Factor(models.Model):
    name = models.CharField(max_length=40, blank=True) 

class Group(models.Model):
    name = models.CharField(max_length=40, blank=True) 

class FactValueOfItem(models.Model):
    fact = models.ForeignKey(Factor, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    val = models.IntegerField(default=-1000) 

class FactValueOfGroup(models.Model):
    fact = models.ForeignKey(Factor, on_delete=models.CASCADE)
    groop = models.ForeignKey(Group, on_delete=models.CASCADE)
    val = models.IntegerField(default=-1000)

class GroupOfItem(models.Model):
    groop = models.ForeignKey(Group, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE) 

class FactorWeightOfProp(models.Model):
    fact = models.ForeignKey(Factor, on_delete=models.CASCADE)
    prop = models.ForeignKey(Page, on_delete=models.CASCADE)
    val = models.IntegerField(default=-1000)

