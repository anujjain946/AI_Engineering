from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def topic_detail(request, topic_slug):
    return HttpResponse(f"You are viewing the topic: {topic_slug}")

def session_detail(request, session_id):
    return HttpResponse(f"You are viewing AI chat session number: {session_id}")
