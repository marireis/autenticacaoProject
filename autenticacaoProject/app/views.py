from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def registrar_usuario(request,template_name="registrar.html"):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        tipo = request.POST['tipo_usuario']
        if tipo == "administrador":
            user = User.objects.create_user(username, email, password)
            user.is_staff = True
            user.save()
        else:
            user = User.objects.create_user(username, email, password)
            return redirect('/listar_usuario/')
        return render(request, template_name, {})

def listar_usuario(request, template_name="listar.html"):
    usuarios = User.objects.all()
    usuario = {'lista': usuarios}
    return render(request,template_name, usuario)