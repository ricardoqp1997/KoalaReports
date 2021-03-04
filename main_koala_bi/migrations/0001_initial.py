# Generated by Django 3.1.7 on 2021-03-03 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Compañía', help_text='Indique el nombre de la entidad a la que se le presta el servicio de informes', max_length=100, unique=True, verbose_name='Nombre de la companía')),
                ('nit', models.IntegerField(help_text='Proporcione el Número Identificador Tributario designado para la entidad', null=True, unique=True, verbose_name='NIT de la entidad')),
                ('bi_link', models.CharField(help_text='Indique el vinculo para compartir el informe de Power BI. Este vinculo se puede encontrar en el portal web de Power BI dentro del informe, usando el botón de "Compartir", seleccoionando la sección de "Insertar informe" y haciendo click nuevamente en el botón "Publicar en la web".', max_length=255, null=True, verbose_name='Vínculo del informe Power BI')),
                ('logo', models.ImageField(help_text='Asigne el logo de su compañía para la identidad del sitio (preferiblemente en formato .PNG o en .SVG para mayor calidad de imagen).', null=True, upload_to='', verbose_name='Logo de la compañía')),
                ('slide1_title', models.CharField(help_text='Indique el titulo del slide 1 del carrusel que se encuentra en la pantalla principal', max_length=50, null=True, verbose_name='Titulo del slide 1 del carrrusel')),
                ('slide2_title', models.CharField(help_text='Indique el titulo del slide 2 del carrusel que se encuentra en la pantalla principal', max_length=50, null=True, verbose_name='Titulo del slide 2 del carrrusel')),
                ('slide3_title', models.CharField(help_text='Indique el titulo del slide 3 del carrusel que se encuentra en la pantalla principal', max_length=50, null=True, verbose_name='Titulo del slide 3 del carrrusel')),
                ('slide1_content', models.TextField(help_text='Indique el contenido de texto del slide 1 del carrusel que se encuentra en la pantalla principal', max_length=400, null=True, verbose_name='Contenido del slide 1 del carrrusel')),
                ('slide2_content', models.TextField(help_text='Indique el contenido de texto del slide 2 del carrusel que se encuentra en la pantalla principal', max_length=400, null=True, verbose_name='Contenido del slide 2 del carrrusel')),
                ('slide1_img', models.ImageField(help_text='Inserte la imagen de fondo del slide 1 de la presentación de su cliente.', null=True, upload_to='', verbose_name='Imagen de slide 1')),
                ('slide2_img', models.ImageField(help_text='Inserte la imagen de fondo del slide 2 de la presentación de su cliente.', null=True, upload_to='', verbose_name='Imagen de slide 2')),
                ('slide3_img', models.ImageField(help_text='Inserte la imagen de fondo del slide 3 de la presentación de su cliente.', null=True, upload_to='', verbose_name='Imagen de slide 3')),
                ('slide3_content', models.TextField(help_text='Indique el contenido de texto del slide 3 del carrusel que se encuentra en la pantalla principal', max_length=400, null=True, verbose_name='Contenido del slide 3 del carrrusel')),
                ('details_maintitle', models.CharField(help_text='Indique el titulo general de la sección de detalles', max_length=50, null=True, verbose_name='Titulo principal de la sección de detalles')),
                ('details_detail', models.TextField(help_text='Indique la descripción general de la sección de detalles', max_length=200, null=True, verbose_name='Descripción de la sección de detalles')),
                ('detail1_title', models.CharField(help_text='Indique el titulo del primer elemento de detalles que se encuentra en la pantalla principal', max_length=50, null=True, verbose_name='Titulo del primer elemento de detalles')),
                ('detail2_title', models.CharField(help_text='Indique el titulo del segundo elemento de detalles que se encuentra en la pantalla principal', max_length=50, null=True, verbose_name='Titulo del segundo elemento de detalles')),
                ('detail3_title', models.CharField(help_text='Indique el titulo del tercer elemento de detalles que se encuentra en la pantalla principal', max_length=50, null=True, verbose_name='Titulo del tercer elemento de detalles')),
                ('detail1_content', models.TextField(help_text='Indique el contenido del primer elemento de detalles que se encuentra en la pantalla principal', max_length=400, null=True, verbose_name='Contenido del primer elemento de detalles')),
                ('detail2_content', models.TextField(help_text='Indique el contenido del segundo elemento de detalles que se encuentra en la pantalla principal', max_length=400, null=True, verbose_name='Contenido del segundo elemento de detalles')),
                ('detail3_content', models.TextField(help_text='Indique el contenido del tercer elemento de detalles que se encuentra en la pantalla principal', max_length=400, null=True, verbose_name='Contenido del tercer elemento de detalles')),
                ('cliente', models.OneToOneField(help_text='Asigne el cliente dueño de el contenido actual', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente propietario')),
            ],
            options={
                'verbose_name': 'Compañía',
            },
        ),
    ]