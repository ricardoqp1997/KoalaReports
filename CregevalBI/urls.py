"""CregevalBI URL Configuration

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

# Importando views base para autenticación
from django.contrib.auth import views as auth_views

# Importando views desde las apps creadas
from login_cregeval_bi import views as login_views
from main_cregeval_bi import views as main_views

# Configuración de nombre y titulos del portal administrativo
admin.site.site_header = 'Administración: Portal de informes'
admin.site.site_title = 'Informes Cregeval'

urlpatterns = [

    # Sitio administrativo
    path('admin/', admin.site.urls),

    # Index
    path('', main_views.index, name='index'),

    # Autenticación
    path('login/', login_views.login_cregeval, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    # Pagina principal y contenido general
    path('main/', main_views.main, name='main'),
    path('main/informes/', main_views.informes, name='informes'),
    path('main/soporte/', main_views.soporte, name='soporte'),

]
