"""usermanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from usermanagementsystem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('mainpage',views.index),
    path('adduser',views.adduser),
    path('homepage',views.homepage),
    # path('homepage/adduser/',views.adduser, name = 'adduser'),
    path('showuser',views.showuser),
    path('showparticularuser',views.showparticularuser),
    path('showparticularuser1',views.showparticularuser1),

    path('deleteuser',views.deleteuser),
    path('deleteuser1',views.deleteuser1),

    path('adddetails',views.addetails),

]
