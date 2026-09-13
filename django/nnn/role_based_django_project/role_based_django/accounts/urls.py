"""
URL configuration for accounts app.
"""
from django.urls import path
from .views import (
    CustomLoginView,
    CustomLogoutView,
    RegisterView,
    dashboard_redirect,
    home,
)

app_name = 'accounts'

urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', dashboard_redirect, name='dashboard'),
]
