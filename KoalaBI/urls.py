"""KoalaBI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Librerías base para administrar URLs
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Modelo base de django para manejo de grupos
from django.contrib.auth.models import Group

# Importando views base para autenticación
from django.contrib.auth import views as auth_views

# Importando views desde las apps creadas
from login_koala_bi import views as login_views
from main_koala_bi import views as main_views

# Configuración de nombre y titulos del portal administrativo
admin.site.site_header = 'Administración: Portal de informes'
admin.site.site_title = 'Informes Koala'

# Se elimina el registro del modelo de grupos porque no se usará
admin.site.unregister(Group)

urlpatterns = [

    # Sitio administrativo
    path('admin/', admin.site.urls),

    # Index
    path('', main_views.index, name='index'),

    # Autenticación
    path('login/', login_views.login_cregeval, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    # Pagina principal y contenido general
    path('main/detalles', main_views.main, name='main'),
    path('main/informes/', main_views.informes, name='informes'),

]

# Configuración del flujo de archivos multimedia cargados en cada formulario de radicación
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
