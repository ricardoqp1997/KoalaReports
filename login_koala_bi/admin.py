# Se importa el metodo admin por defecto
from django.contrib import admin

# Modelo creado para manejo personalizado de usuarios
from login_koala_bi.models import CregevalUSer


# Se crea una clase para customizar la vista en panel administrativo del modelo de usuarios
class CregevalUsersAdmin(admin.ModelAdmin):

    # Visualización de columnas del modelo de usuarios
    list_display = ['username', 'email', 'first_name']

    # Columnas configuradas para orgnización, filtrado y búsqueda de usuarios
    list_filter = ['username', 'email']
    search_fields = list_filter
    ordering = ['username']

    # Campos a mostrar en el usuario seleccionado
    fieldsets = (
        (
            'Datos de acceso', {
                'fields': ['username', 'email', 'password']
            }
        ),
        (
            'Información de la cuenta', {
                'fields': ['first_name']
            }
        ),
        (
            'Permisos de usuario', {
                'fields': ['is_superuser', 'is_staff', 'is_active']
            }
        )
    )

    # Campos de solo lectura (Contraseña ineditable en este campo)
    readonly_fields = ['password']

    # Se determina que no habrá posibilidad de crear nuevos usuarios por este medio, solo por consola
    def has_add_permission(self, request):
        return False


# Se hace el registro del modelo de usuarios y de su vista en el panel administrativo
admin.site.register(CregevalUSer, CregevalUsersAdmin)
