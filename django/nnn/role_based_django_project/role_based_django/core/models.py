"""
Core models for menu system.
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Role


class MenuItem(models.Model):
    """
    Dynamic menu items stored in database.
    Can be assigned to specific roles.
    """
    title = models.CharField(_('title'), max_length=100)
    url = models.CharField(_('URL'), max_length=200)
    icon = models.CharField(_('icon class'), max_length=100, blank=True, default='fa-circle')
    order = models.PositiveIntegerField(_('order'), default=0)
    is_active = models.BooleanField(_('active'), default=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('parent menu')
    )
    roles = models.ManyToManyField(
        'accounts.RoleAssignment',
        blank=True,
        related_name='menu_items',
        verbose_name=_('visible to roles')
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = _('menu item')
        verbose_name_plural = _('menu items')

    def __str__(self):
        return self.title

    def get_children(self):
        """Get child menu items."""
        return self.children.filter(is_active=True)

    def has_children(self):
        """Check if menu item has children."""
        return self.children.filter(is_active=True).exists()


class RoleAssignment(models.Model):
    """
    Role assignment model for many-to-many relationship.
    """
    role = models.CharField(_('role'), max_length=10, choices=Role.choices, unique=True)

    class Meta:
        verbose_name = _('role assignment')
        verbose_name_plural = _('role assignments')

    def __str__(self):
        return self.role
