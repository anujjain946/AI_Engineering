from django.core.management.base import BaseCommand
from menus.models import MenuItem

class Command(BaseCommand):
    help = "Create default dynamic menu items."

    def handle(self, *args, **options):
        items = [
            ("Dashboard", "dashboard", "dashboard", "dashboard.view", 1),
            ("Movies", "movies", "movies", "movies.view", 2),
            ("Users", "users", "custom_admin:accounts_user_changelist", "users.view", 3),
            ("Roles", "roles", "custom_admin:rbac_role_changelist", "roles.manage", 4),
            ("Menu Management", "menus", "custom_admin:menus_menuitem_changelist", "menus.manage", 5),
        ]
        for name, code, url_name, permission, sort in items:
            MenuItem.objects.update_or_create(
                code=code,
                defaults={
                    "name": name,
                    "url_name": url_name,
                    "required_permission": permission,
                    "sort_order": sort,
                    "is_active": True,
                },
            )
        self.stdout.write(self.style.SUCCESS("Menus seeded."))
