"""rep-test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('', include(('regandauth.urls', 'regandauth'), namespace='regandauth')),
    path('', include(('sandbox.urls', 'sandbox'), namespace='sandbox')),
    path('', include('social_django.urls')),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("addpeople/", include(('addpeople.urls', 'addpeople'), namespace='addpeople')),
    path("estpeople/", include(('estpeople.urls', 'estpeople'), namespace='estpeople')),
    path("results/", include(('results.urls', 'results'), namespace='results')),
    path("stats/", views.stats, name="stats"),
]
 
handler404 = 'main.views.view_404' 
