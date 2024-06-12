from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            message = f'{user.username}'
            return redirect("users:login",{"message":message})
        
    form = UserCreationForm()

    return render(request, "login/register.html", {"form": form})


def login(request):
    return render(request, "login/login.html")

