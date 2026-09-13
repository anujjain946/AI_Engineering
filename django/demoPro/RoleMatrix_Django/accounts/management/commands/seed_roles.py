from django.core.management.base import BaseCommand
from accounts.models import Role, Permission

DATA={
"Admin":["dashboard.view","users.view","reports.view","settings.view"],
"Manager":["dashboard.view","users.view","reports.view"],
"Staff":["dashboard.view","reports.view"],
"Customer":["dashboard.view"],
}
class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        for role_name,codes in DATA.items():
            role,_=Role.objects.get_or_create(name=role_name,slug=role_name.lower())
            for code in codes:
                perm,_=Permission.objects.get_or_create(code=code,defaults={"name":code.replace("."," ").title()})
                from accounts.models import RolePermission
                RolePermission.objects.get_or_create(role=role,permission=perm)
        self.stdout.write(self.style.SUCCESS("Roles and permissions seeded."))
        self.stdout.write("Create users from /admin/ and assign a role.")
