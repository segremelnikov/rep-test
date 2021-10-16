# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("<int:cur_step>", views.render_step, name="render_step"),
    path("<int:cur_step>/", views.render_step, name="render_step1"),
    path("", views.index, name="index"),
    path("savesettings/", views.savesettings, name="savesettings"),
    path("saveitem/", views.saveitem, name="saveitem"),
    path("savequestion/", views.savequestion, name="savequestion"),
    path("<int:user_id>/<int:cur_step>", views.show_people, name="show_people"),
    path("<int:user_id>/<int:cur_step>/", views.show_people, name="show_people1"),
]