from django.db import models
from django.contrib.auth.models import AbstractUser


# Modelo para gestión de usuarios en Django y SQLite
class CregevalUSer(AbstractUser):

    email = models.EmailField(
        verbose_name='Correo electrónico',
        help_text='Ingrese el correo electrónico de su cuenta',
        unique=True
    )

    first_name = models.CharField(
        verbose_name='Nombre',
        help_text='Indique su nombre',
        max_length=100
    )

    last_name = models.CharField(
        verbose_name='Apellidos',
        help_text='Indique sus apellidos',
        max_length=100
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]
