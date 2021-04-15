from django.db import models
from login_koala_bi.models import CregevalUSer


# Aquí se designaran los privilegios y sus tipos existentes en el portal, para accesos y prioridades
class CompanyContent(models.Model):
    """------------------------- DATOS DE LA ENTIDAD DEL CLIENTE ---------------------------------------"""

    cliente = models.OneToOneField(
        CregevalUSer,
        on_delete=models.CASCADE,
        verbose_name='Cliente propietario',
        help_text='Asigne el cliente dueño de el contenido actual',
        unique=True
    )

    name = models.CharField(
        verbose_name='Nombre de la companía',
        help_text='Indique el nombre de la entidad a la que se le presta el servicio de informes',
        max_length=100,
        unique=True,
        default='Compañía',
    )

    nit = models.BigIntegerField(
        verbose_name='NIT de la entidad',
        help_text='Proporcione el Número Identificador Tributario designado para la entidad',
        unique=True,
        null=True,
    )

    """"------------------------- INFORMACIÓN DE INFORMES DEL CLiENTE -----------------------------------"""

    bi_link = models.CharField(
        verbose_name='Vínculo del informe Power BI',
        help_text='Indique el vinculo para compartir el informe de Power BI. Este vinculo se puede encontrar '
                  'en el portal web de Power BI dentro del informe, usando el botón de "Compartir", seleccoionando la '
                  'sección de "Insertar informe" y haciendo click nuevamente en el botón "Publicar en la web".',
        max_length=255,
        null=True
    )

    """"------------------------- CONTENIDO DE LA ENTIDAD DEL CLiENTE -----------------------------------"""

    # Logo
    logo = models.ImageField(
        verbose_name='Logo de la compañía',
        help_text='Asigne el logo de su compañía para la identidad del sitio (preferiblemente en formato .PNG o '
                  'en .SVG para mayor calidad de imagen).',
        null=True
    )

    # Carousel mainpage
    slide1_title = models.CharField(
        verbose_name='Titulo del slide 1 del carrrusel',
        help_text='Indique el titulo del slide 1 del carrusel que se encuentra en la pantalla principal',
        max_length=50,
        null=True
    )

    slide2_title = models.CharField(
        verbose_name='Titulo del slide 2 del carrrusel',
        help_text='Indique el titulo del slide 2 del carrusel que se encuentra en la pantalla principal',
        max_length=50,
        null=True
    )

    slide3_title = models.CharField(
        verbose_name='Titulo del slide 3 del carrrusel',
        help_text='Indique el titulo del slide 3 del carrusel que se encuentra en la pantalla principal',
        max_length=50,
        null=True
    )

    slide1_content = models.TextField(
        verbose_name='Contenido del slide 1 del carrrusel',
        help_text='Indique el contenido de texto del slide 1 del carrusel que se encuentra en la pantalla principal',
        max_length=400,
        null=True
    )

    slide2_content = models.TextField(
        verbose_name='Contenido del slide 2 del carrrusel',
        help_text='Indique el contenido de texto del slide 2 del carrusel que se encuentra en la pantalla principal',
        max_length=400,
        null=True
    )

    slide1_img = models.ImageField(
        verbose_name='Imagen de slide 1',
        help_text='Inserte la imagen de fondo del slide 1 de la presentación de su cliente.',
        null=True
    )

    slide2_img = models.ImageField(
        verbose_name='Imagen de slide 2',
        help_text='Inserte la imagen de fondo del slide 2 de la presentación de su cliente.',
        null=True
    )

    slide3_img = models.ImageField(
        verbose_name='Imagen de slide 3',
        help_text='Inserte la imagen de fondo del slide 3 de la presentación de su cliente.',
        null=True
    )

    slide3_content = models.TextField(
        verbose_name='Contenido del slide 3 del carrrusel',
        help_text='Indique el contenido de texto del slide 3 del carrusel que se encuentra en la pantalla principal',
        max_length=400,
        null=True
    )

    # Details mainpage
    details_maintitle = models.CharField(
        verbose_name='Titulo principal de la sección de detalles',
        help_text='Indique el titulo general de la sección de detalles',
        max_length=50,
        null=True
    )

    details_detail = models.TextField(
        verbose_name='Descripción de la sección de detalles',
        help_text='Indique la descripción general de la sección de detalles',
        max_length=200,
        null=True
    )

    detail1_title = models.CharField(
        verbose_name='Titulo del primer elemento de detalles',
        help_text='Indique el titulo del primer elemento de detalles que se encuentra en la pantalla principal',
        max_length=50,
        null=True
    )

    detail2_title = models.CharField(
        verbose_name='Titulo del segundo elemento de detalles',
        help_text='Indique el titulo del segundo elemento de detalles que se encuentra en la pantalla principal',
        max_length=50,
        null=True
    )

    detail3_title = models.CharField(
        verbose_name='Titulo del tercer elemento de detalles',
        help_text='Indique el titulo del tercer elemento de detalles que se encuentra en la pantalla principal',
        max_length=50,
        null=True
    )

    detail1_content = models.TextField(
        verbose_name='Contenido del primer elemento de detalles',
        help_text='Indique el contenido del primer elemento de detalles que se encuentra en la pantalla principal',
        max_length=400,
        null=True
    )

    detail2_content = models.TextField(
        verbose_name='Contenido del segundo elemento de detalles',
        help_text='Indique el contenido del segundo elemento de detalles que se encuentra en la pantalla principal',
        max_length=400,
        null=True
    )

    detail3_content = models.TextField(
        verbose_name='Contenido del tercer elemento de detalles',
        help_text='Indique el contenido del tercer elemento de detalles que se encuentra en la pantalla principal',
        max_length=400,
        null=True
    )

    REQUIRED_FIELD = [
        'cliente',
        'name',

    ]

    class Meta:
        verbose_name = 'Compañía'

    def __str__(self):
        return str(self.id)

