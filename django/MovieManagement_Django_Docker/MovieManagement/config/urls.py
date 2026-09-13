from django.urls import include, path
from core.views import home, login_view, logout_view, dashboard
from core.movie_views import movies_dashboard
from core.admin_site import custom_admin_site
import core.admin_register  # noqa: F401

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("movies/", movies_dashboard, name="movies"),
    path("admin/", custom_admin_site.urls),
    path("api/", include("core.api_urls")),
]
