"""stuck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
<<<<<<< HEAD
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('accounts/', include('allauth.urls')),
    url('ecommerce/', include('ecommerce.urls')),
=======
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ecommerce/', include('ecommerce.urls')),
    path('influence/', include('influence.urls')),
>>>>>>> 4e66cf057722518e31a4ffcd41c30b2d6691da3f
]
