from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'login/register.html')

def login(request):
    return render(request,'login/login.html')
    
def user(request):
    # Definir una lambda para formatear el mensaje
    format_message = lambda name: f"Usuario {name} registrado con éxito."

    # Ejemplo de uso de la lambda
    user_name = "Alice"  # Este valor vendría del request en una aplicación real
    message = format_message(user_name)
    
    return render(request, 'user/profile.html', {'message': message})

