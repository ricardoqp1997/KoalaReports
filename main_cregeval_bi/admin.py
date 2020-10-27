# Se importa el metodo admin por defecto
from django.contrib import admin

# Modelo creado para manejo de privilegios
from main_cregeval_bi.models import CregevalCastType


# Se crea una clase para customizar la vista en panel administrativo del modelo de privilegios.
class CregevalCastAdmin(admin.ModelAdmin):

    # Visualización de columnas del modelo de privilegios
    list_display = ['id', 'privilegio']

    # Columnas configuradas para orgnización, filtrado y búsqueda de privilegios
    list_filter = list_display
    search_fields = list_display
    ordering = ['id']

    # Campos a mostrar en el privilegio seleccionado
    fieldsets = (
        (
            'Indique el nombre del privilegio', {
                'fields': ['privilegio']
            }
        ),
    )


# Se hace el registro del modelo de privilegios y de su vista en el panel administrativo
admin.site.register(CregevalCastType, CregevalCastAdmin)
