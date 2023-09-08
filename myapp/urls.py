# This is myapp urls.py
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_view

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.loginsuccess, name='loginsuccess'),
]