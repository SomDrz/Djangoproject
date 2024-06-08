"""
URL configuration for empy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from atexit import register
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path("about/",about),
    path("add/",add),
    path("delete-emp/<int:emp_id>",deleteEmp),
    path("update-emp/<int:emp_id>",updateEmpPage), #render page
    path("update/<int:emp_id>",updateEmp), # updating
    path("search/",Search),
    path("login/",login_Page),
    path("register/",register),
    path("logout/",logout_Page)

]