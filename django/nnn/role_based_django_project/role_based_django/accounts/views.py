"""
Views for user authentication.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import Role

User = get_user_model()


class CustomLoginView(LoginView):
    """Custom login view with role-based redirection."""
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    redirect_field_name = 'next'

    def get_success_url(self):
        """Redirect to role-specific dashboard."""
        user = self.request.user
        return user.get_dashboard_url()


class CustomLogoutView(LogoutView):
    """Custom logout view."""
    next_page = reverse_lazy('login')


class RegisterView(CreateView):
    """User registration view."""
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully! Please login.')
        return response

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


@login_required
def dashboard_redirect(request):
    """Redirect to role-specific dashboard."""
    return redirect(request.user.get_dashboard_url())


def home(request):
    """Home page view."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'accounts/home.html')
