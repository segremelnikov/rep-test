from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    secret_code = models.CharField(max_length=3)
    has_added_people = models.BooleanField(default=False)
    has_estimeted_people = models.BooleanField(default=False)
    current_estimate_step = models.IntegerField(default=0) 
    background_image_index = models.IntegerField(default=0)
    background_color = models.CharField(max_length=8, default='#ffffff')
    backgruond_opacity = models.IntegerField(default=100)
    fontcolor = models.CharField(max_length=8, default='#000000')
    tickline_color = models.CharField(max_length=8, default='#9b5ab1')
    imptickline_color = models.CharField(max_length=8, default='#4169c8')
    tickline_lbl_color = models.CharField(max_length=8, default='#69a5ff')
    imptickline_lbl_color = models.CharField(max_length=8, default='#be96ff')
    speed = models.FloatField(default=1)
    df = models.TextField(blank=True, default="")


    def __str__(self):
        return str(self.user) + " -- data "


class UserEntry(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.CharField(max_length=16, default='#')
    ip = models.CharField(max_length=16, default='#')
    datetime = models.CharField(max_length=40, default='#')
    width = models.CharField(max_length=10, default='#')
    height = models.CharField(max_length=10, default='#')
    os = models.CharField(max_length=30, default='#')
    browser = models.CharField(max_length=30, default='#')
    is_mob = models.BooleanField(default=False)
    tz = models.CharField(max_length=50, default="#")


    def __str__(self):
        return str(self.user) + " -- " + str(self.datetime) + " (" + str(self.page) + ") " + str(self.width) + "-" + str(self.height)


class AnonEntry(models.Model):

    page = models.CharField(max_length=16, default='#')
    ip = models.CharField(max_length=16, default='#')
    datetime = models.CharField(max_length=40, default='#')
    width = models.CharField(max_length=10, default='#')
    height = models.CharField(max_length=10, default='#')
    os = models.CharField(max_length=30, default='#')
    browser = models.CharField(max_length=30, default='#')
    is_mob = models.BooleanField(default=False)
    tz = models.CharField(max_length=50, default="#")

    def __str__(self):
        return str(self.ip) + " -- " + str(self.datetime) + " (" + str(self.page) + ")" + str(self.width) + "-" + str(self.height)




