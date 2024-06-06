from django.urls import path
from . import views  

app_name = "users"

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("user/", views.user, name='user'),
]

