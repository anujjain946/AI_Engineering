"""
URL configuration for core app.
"""
from django.urls import path
from .views import admin_dashboard, manager_dashboard, customer_dashboard

app_name = 'core'

urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('manager-dashboard/', manager_dashboard, name='manager_dashboard'),
    path('customer-dashboard/', customer_dashboard, name='customer_dashboard'),
]
