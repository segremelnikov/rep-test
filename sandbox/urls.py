from django.urls import  path
from django.views.generic import TemplateView

from . import views

urlpatterns = [ 
    path('.well-known/pki-validation/A793AD14D9369B4B26D1A02C83AAB015.txt', views.txt),
    path("plot/", views.plot, name="plot"),
    path("plot/<int:id>", views.plot, name="plot1"),
    path("plot/<int:id>/", views.plot, name="plot2"),
    path("plot/<int:id>/<int:nf>", views.plot, name="plot3"),
    path("plot/<int:id>/<int:nf>/", views.plot, name="plot4"),
    path("sa/", views.show_ans, name="sa"),
    path("sa/<int:id>", views.show_ans, name="sa1"),
]