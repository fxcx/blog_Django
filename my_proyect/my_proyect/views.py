# from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    # username = request.session.get('username', None)  # Obtén el nombre de usuario de la sesión
    username = request.GET.get('username', None)  # Obtén el nombre de usuario de los parámetros de la URL
    return render(request, "index.html", {"username":username})

def about_page(request):
    return render(request, "about.html")