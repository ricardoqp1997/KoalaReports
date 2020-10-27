from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from login_cregeval_bi.models import CregevalUSer


# redireccionamiento de la pagina respecto a la autenticación del usuario
def index(request):
    if request.user.is_authenticated:
        return redirect('/main/')
    else:
        logout(request)
        return redirect('login/')


# Vista de la pagina principal del portal
@login_required(login_url='http://127.0.0.1:8000/login/')
def main(request):

    name = request.user.get_full_name()

    if request.user.is_authenticated:

        global user

        context_inicio = {
            'title': 'Informes Cregeval - Pagina principal',
            'user_name': name
        }
        return render(request, 'main.html', context_inicio)
    else:
        return redirect('/login/')


# Vista de la sección de informes del portal
@login_required(login_url='http://127.0.0.1:8000/login/')
def informes(request):

    type_user = CregevalUSer.objects.get(privilegio_user_id=request.user.id).privilegio_user
    print(type_user)
    if request.user.is_authenticated:

        context_inicio = {
            'title': 'Informes Cregeval - Vista de informes',
            'type_user': type_user
        }
        return render(request, 'informes.html', context_inicio)
    else:
        return redirect('/login/')


# Vista de la sección de soporte y ayuda del portal
@login_required(login_url='http://127.0.0.1:8000/login/')
def soporte(request):

    if request.user.is_authenticated:

        global user

        context_inicio = {
            'title': 'Informes Cregeval - Soporte y ayuda',
        }
        return render(request, 'soporte.html', context_inicio)
    else:
        return redirect('/login/')
