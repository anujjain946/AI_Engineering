"""
Views for core app - dashboards and menu.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import MenuItem


@login_required
def admin_dashboard(request):
    """Admin dashboard view."""
    return render(request, 'core/admin_dashboard.html', {
        'page_title': 'Admin Dashboard'
    })


@login_required
def manager_dashboard(request):
    """Manager dashboard view."""
    return render(request, 'core/manager_dashboard.html', {
        'page_title': 'Manager Dashboard'
    })


@login_required
def customer_dashboard(request):
    """Customer dashboard view."""
    return render(request, 'core/customer_dashboard.html', {
        'page_title': 'Customer Dashboard'
    })
