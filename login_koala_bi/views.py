from django.contrib import messages
from django.shortcuts import render, redirect

# Módulos para la manipulación de usuarios
from django.contrib.auth import (
    authenticate,
    login,
)

# Módulos de forms.py
from .forms import (
    UserLoginForm,
)

import datetime


# Vista de inicio de sesión al portal
def login_cregeval(request):

    form = UserLoginForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        login(request, user)

        return redirect('/main/informes')

    login_context = {
        'form': form,
        'title': 'Informes Koala',
        'year': datetime.date.today().year
    }

    print(datetime.date.today().year)

    return render(request, 'login.html', login_context)
