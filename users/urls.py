from django.urls import path
from . import views

app_name = "users"  # Namespace for URL names


urlpatterns = [
    path("register/", views.user_reg, name="register"),
    path("login/", views.user_log, name="login"),
    path("logout/", views.user_logout, name="logout"),
   ]
