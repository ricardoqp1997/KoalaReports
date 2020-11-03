# Se importa el metodo admin por defecto
from django.contrib import admin

# Modelo creado para manejo de privilegios
from main_cregeval_bi.models import CompanyContent


# Se crea una clase para customizar la vista en panel administrativo del modelo de privilegios.
class CregevalCastAdmin(admin.ModelAdmin):

    # Visualización de columnas del modelo de privilegios
    list_display = ['id', 'nit', 'name', 'cliente']

    # Columnas configuradas para orgnización, filtrado y búsqueda de privilegios
    list_filter = list_display
    search_fields = list_display
    ordering = ['id', ]

    # Campos a mostrar en el privilegio seleccionado
    fieldsets = (
        (
            'Datos de la entidad del cliente', {
                'fields': ['cliente', 'name', 'nit', ]
            }
        ),
        (
            'Información de informes del cliente', {
                'fields': ['bi_link', ]
            }
        ),
        (
            'Contenido de la entidad del cliente: Logotipo', {
                'fields': ['logo', ]
            }
        ),
        (
            'Contenido de la entidad del cliente: Carrusel inicial', {
                'fields': [
                    'slide1_title',
                    'slide1_content',
                    'slide1_img',

                    'slide2_title',
                    'slide2_content',
                    'slide2_img',

                    'slide3_title',
                    'slide3_content',
                    'slide3_img',
                ]
            }
        ),
        (
            'Contenido de la entidad del cliente: Detalles', {
                'fields': [
                    'details_maintitle',
                    'details_detail',

                    'detail1_title',
                    'detail1_content',

                    'detail2_title',
                    'detail2_content',

                    'detail3_title',
                    'detail3_content',
                ]
            }
        ),
    )


# Se hace el registro del modelo de privilegios y de su vista en el panel administrativo
admin.site.register(CompanyContent, CregevalCastAdmin)
