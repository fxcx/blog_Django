from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("users:login")
        
    form = UserCreationForm()

    return render(request, "login/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # request.session['username'] = user.username  # Guarda el nombre de usuario en la sesión
            # return  redirect("/")
            return redirect(f"{reverse('users:home')}?username={user.username}")
        else:
            form = AuthenticationForm()
            message = "Usuario o contraseña incorrectos"
            return render(request, "login/login.html", {"form": form,"message":message})
    
    form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})

