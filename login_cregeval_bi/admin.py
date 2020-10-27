# Se importa el metodo admin por defecto
from django.contrib import admin

# Modelo creado para manejo personalizado de usuarios
from login_cregeval_bi.models import CregevalUSer


# Se crea una clase para customizar la vista en panel administrativo del modelo de usuarios
class CregevalUsersAdmin(admin.ModelAdmin):
    pass


# Se hace el registro del modelo de usuarios y de su vista en el panel administrativo
admin.site.register(CregevalUSer, CregevalUsersAdmin)
