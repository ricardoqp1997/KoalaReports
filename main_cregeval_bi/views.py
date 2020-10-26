from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


user = None


# redireccionamiento de la pagina respecto a la autenticación del usuario
def index(request):
    if request.user.is_authenticated:
        return redirect('/main/')
    else:
        logout(request)
        return redirect('login/')


@login_required(login_url='http://127.0.0.1:8000/login/')
def main(request):

    if request.user.is_authenticated:

        global user

        context_inicio = {
            'title': 'Informes Cregeval - Pagina principal',
        }
        return render(request, 'main.html', context_inicio)
    else:
        return redirect('/login/')


@login_required(login_url='http://127.0.0.1:8000/login/')
def informes(request):

    if request.user.is_authenticated:

        global user

        context_inicio = {
            'title': 'Informes Cregeval - Vista de informes',
        }
        return render(request, 'informes.html', context_inicio)
    else:
        return redirect('/login/')


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
