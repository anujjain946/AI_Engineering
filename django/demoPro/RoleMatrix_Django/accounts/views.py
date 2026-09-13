from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.user.is_authenticated: return redirect("/")
    if request.method=="POST":
        email=request.POST.get("email","").strip()
        password=request.POST.get("password","")
        role_slug=request.POST.get("role","")
        user=authenticate(request,email=email,password=password)
        if user and user.is_active and user.role and user.role.slug==role_slug:
            login(request,user); return redirect("/")
        messages.error(request,"Invalid email, password, or role.")
    from .models import Role
    return render(request,"login.html",{"roles":Role.objects.filter(is_active=True)})

def logout_view(request):
    logout(request); return redirect("/login/")
