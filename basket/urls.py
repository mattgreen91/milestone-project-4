from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<product_sku>/', views.add_to_basket, name='add_to_basket'),
    path('modify/<product_sku>/', views.modify_basket, name='modify_basket'),
    path('remove/<product_sku>/', views.remove_from_basket, name='remove_from_basket'),
]
