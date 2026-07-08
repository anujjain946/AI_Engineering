from django.urls import path 
from . import views 
urlpatterns = [ 
    path('', views.home, name='home'),
     # Captures an integer ID from the URL (e.g., chat/session/4/)
    path('session/<int:session_id>/', views.session_detail, name='session_detail'),
    
    # Captures a string slug from the URL (e.g., chat/topic/ai-tools/)
    path('topic/<slug:topic_slug>/', views.topic_detail, name='topic_detail'),

    path('home/', views.home, name='home'),

 ]
