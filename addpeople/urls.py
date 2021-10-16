# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("<int:user_id>", views.show_people, name="show_people"),
    path("<int:user_id>/", views.show_people, name="show_people1"),
    path("", views.index, name="index"),
]