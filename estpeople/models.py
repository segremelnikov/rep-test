from django.db import models
from django.contrib.auth.models import User
from addpeople.models import Item


class Page(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(default=-1)
    first1 = models.CharField(max_length=30, default='', blank=True)
    second1 = models.CharField(max_length=30, default='', blank=True)
    third1 = models.CharField(max_length=30, default='', blank=True)
    first_item1 = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name="first_item1", null=True)
    second_item1 = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name="second_item1", null=True)
    third_item1 = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name="third_item1", null=True)
    two_like1 = models.BooleanField(default=False)
    third_chosen1 = models.IntegerField(default=-1)
    prop1 = models.CharField(max_length=40, blank=True)
    first2 = models.CharField(max_length=30, default='', blank=True)
    second2 = models.CharField(max_length=30, default='', blank=True)
    third2 = models.CharField(max_length=30, default='', blank=True)
    first_item2 = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name="first_item2", null=True)
    second_item2 = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name="second_item2", null=True)
    third_item2 = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name="third_item2", null=True)
    two_like2 = models.BooleanField(default=False)
    third_chosen2 = models.IntegerField(default=-1)
    prop2 = models.CharField(max_length=40, blank=True)
    first3 = models.CharField(max_length=30, default='', blank=True)
    second3 = models.CharField(max_length=30, default='', blank=True)
    third3 = models.CharField(max_length=30, default='', blank=True)
    first_item3 = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name="first_item3", null=True)
    second_item3 = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name="second_item3", null=True)
    third_item3 = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name="third_item3", null=True)
    two_like3 = models.BooleanField(default=False)
    third_chosen3 = models.IntegerField(default=-1)
    prop3 = models.CharField(max_length=40, blank=True)
    index = models.IntegerField(default=0)
    prop_name = models.CharField(max_length=40, blank=True)
    cur_item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name="cur_item", null=True)
    is_saved = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.user) + " -- " + str(self.prop_name) + " -- " + str(self.number) + " (" + str(self.is_saved) + ")"

class Estimation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    number = models.IntegerField(default=-1)
    value = models.IntegerField(default=-1000)
    x = models.FloatField(default=-1000)
    y = models.FloatField(default=-1000)

    def __str__(self):
        return str(self.item) + ", " + str(self.number) + ": " + str(self.value)


