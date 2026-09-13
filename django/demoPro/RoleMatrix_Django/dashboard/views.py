from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    menu=[]
    if request.user.is_superuser or request.user.has_role_permission("dashboard.view"):
        menu.append(("Dashboard","/"))
    if request.user.is_superuser or request.user.has_role_permission("users.view"):
        menu.append(("Users","/#users"))
    if request.user.is_superuser or request.user.has_role_permission("reports.view"):
        menu.append(("Reports","/#reports"))
    if request.user.is_superuser or request.user.has_role_permission("settings.view"):
        menu.append(("Settings","/#settings"))
    return render(request,"dashboard.html",{"menu":menu})
