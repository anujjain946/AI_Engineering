from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rbac.models import Permission, Role, RolePermission, UserRole

class Command(BaseCommand):
    help = "Create default roles, permissions and demo users."

    def handle(self, *args, **options):
        permissions = [
            ("View Dashboard", "dashboard.view"),
            ("View Movies", "movies.view"),
            ("Manage Movies", "movies.manage"),
            ("View Users", "users.view"),
            ("Manage Users", "users.manage"),
            ("Manage Menus", "menus.manage"),
            ("Manage Roles", "roles.manage"),
        ]

        permission_objects = {}
        for name, code in permissions:
            obj, _ = Permission.objects.get_or_create(
                code=code, defaults={"name": name}
            )
            permission_objects[code] = obj

        roles = {
            "ADMIN": ["dashboard.view", "movies.view", "movies.manage", "users.view",
                      "users.manage", "menus.manage", "roles.manage"],
            "STAFF": ["dashboard.view", "movies.view", "movies.manage"],
            "VIEWER": ["dashboard.view", "movies.view"],
        }

        role_objects = {}
        for code, perm_codes in roles.items():
            role, _ = Role.objects.get_or_create(
                code=code, defaults={"name": code.title()}
            )
            role_objects[code] = role
            for perm_code in perm_codes:
                RolePermission.objects.get_or_create(
                    role=role, permission=permission_objects[perm_code]
                )

        User = get_user_model()

        admin_user, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@example.com",
                "is_staff": True,
                "is_superuser": True,
                "is_admin_user": True,
            },
        )
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.is_admin_user = True
        if created:
            admin_user.set_password("Admin@123")
        admin_user.save()
        UserRole.objects.get_or_create(user=admin_user, role=role_objects["ADMIN"])

        demo_user, created = User.objects.get_or_create(
            username="user",
            defaults={"email": "user@example.com"},
        )
        if created:
            demo_user.set_password("User@123")
            demo_user.save()
        UserRole.objects.get_or_create(user=demo_user, role=role_objects["VIEWER"])

        self.stdout.write(self.style.SUCCESS("RBAC seeded."))
        self.stdout.write("Admin: admin / Admin@123")
        self.stdout.write("User : user / User@123")
