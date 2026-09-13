"""
User models with role-based authentication.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.TextChoices):
    ADMIN = 'admin', _('Admin')
    MANAGER = 'manager', _('Manager')
    CUSTOMER = 'customer', _('Customer')


class User(AbstractUser):
    """
    Custom User model with email, contact, and role fields.
    Email is used as the unique identifier for authentication.
    """
    email = models.EmailField(_('email address'), unique=True)
    contact = models.CharField(_('contact number'), max_length=15, blank=True, null=True)
    role = models.CharField(
        _('role'),
        max_length=10,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )
    is_email_verified = models.BooleanField(_('email verified'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.role == Role.ADMIN

    @property
    def is_manager(self):
        return self.role == Role.MANAGER

    @property
    def is_customer(self):
        return self.role == Role.CUSTOMER

    def get_dashboard_url(self):
        """Return dashboard URL based on user role."""
        from django.urls import reverse
        if self.is_admin:
            return reverse('admin_dashboard')
        elif self.is_manager:
            return reverse('manager_dashboard')
        else:
            return reverse('customer_dashboard')
