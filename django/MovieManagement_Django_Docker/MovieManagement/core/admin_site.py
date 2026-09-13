from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth import login
from django.contrib.admin.forms import AdminAuthenticationForm
from django.shortcuts import redirect, render

class CustomAdminSite(AdminSite):
    site_header = "MovieManagement Administration"
    site_title = "MovieManagement Admin"
    index_title = "Administration Dashboard"
    login_template = "admin/custom_login.html"

    def has_permission(self, request):
        return bool(
            request.user.is_authenticated
            and request.user.is_active
            and (request.user.is_staff or request.user.is_superuser)
        )

    def login(self, request, extra_context=None):
        if request.method == "POST":
            form = AdminAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                if not (user.is_staff or user.is_superuser):
                    form.add_error(None, "Admin access is not enabled for this user.")
                else:
                    login(request, user)
                    return redirect(request.GET.get("next") or self.index_path)
        else:
            form = AdminAuthenticationForm(request)
        context = {
            **self.each_context(request),
            "form": form,
            "title": "Admin Login",
            **(extra_context or {}),
        }
        return render(request, self.login_template, context)

custom_admin_site = CustomAdminSite(name="custom_admin")
