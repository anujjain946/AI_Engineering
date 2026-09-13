from django.urls import path
from .api_views import MeAPIView, MenuAPIView

urlpatterns = [
    path("me/", MeAPIView.as_view(), name="api-me"),
    path("menus/", MenuAPIView.as_view(), name="api-menus"),
]
