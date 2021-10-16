from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.register),
    path('check_login/', views.check_login, name='check_login'),
    path('check_email/', views.check_email, name='check_email'),
    path('check_password/', views.check_password, name='check_password'),
    path('check_code/', views.check_code, name='check_code'),
    path('sendcode/', views.sendcode, name='sendcode'),
]