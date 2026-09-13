from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def movies_dashboard(request):
    return render(request, "movies/dashboard.html")
