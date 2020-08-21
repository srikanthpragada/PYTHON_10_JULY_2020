from django.contrib import admin
from django.urls import path
from . import views, ajax_views

urlpatterns = [
    path('index/', views.index),
    path('about/', views.about),
    path('employees/', views.list_employees),
    path('countries/', views.list_countries),
    path('updatesalary/', views.update_salary),
    path('add/', views.add_employee),
    path('ajax/', ajax_views.ajax_demo),
    path('quote/', ajax_views.get_quote),
]
