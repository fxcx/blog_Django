from django.urls import path
from . import views  

app_name = "users"

urlpatterns = [
    path("", views.user, name='user'),
    
    path("register", views.register, name="register"),
    path("login/", views.login, name="login"),
]

