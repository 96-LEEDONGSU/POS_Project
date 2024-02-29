# This is myapp urls.py
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_view

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.loginsuccess, name='loginsuccess'),
    path('productlist/', views.productlist, name='productlist'),
    path('productadd/', views.productadd, name='productadd'),
    path('customerlist/', views.customerlist, name='customerlist'),
    path('modify/<id>/', views.customer_modify, name='customer_modify'),
    path('customerlist', views.modifyMemberData, name='modifyMemberData'),
    path('add-member/', views.customer_add, name='customer_add'),
    path('customerdelete/<int:c_idx>/', views.customer_delete, name='customer_delete'),
]