# Se importa el metodo admin por defecto
from django.contrib import admin

# Modelo creado para manejo de privilegios
from main_cregeval_bi.models import CregevalCastType

# Modelo base de django para manejo de grupos
from django.contrib.auth.models import Group


# Se crea una clase para customizar la vista en panel administrativo del modelo de privilegios.
class CregevalCastAdmin(admin.ModelAdmin):
    pass


# Se hace el registro del modelo de privilegios y de su vista en el panel administrativo
admin.site.register(CregevalCastType, CregevalCastAdmin)
# Se elimina el registro del modelo de grupos porque no se usará
admin.site.unregister(Group)
