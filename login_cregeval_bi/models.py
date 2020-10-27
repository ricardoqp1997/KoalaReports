from django.db import models
from django.contrib.auth.models import AbstractUser
from main_cregeval_bi.models import CregevalCastType


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

    privilegio_user = models.ForeignKey(
        CregevalCastType,
        null=True,
        verbose_name='Privilegio asignado',
        help_text='Designe entre los privilegios existentes, el que sea requerido para el usuario',
        on_delete=models.SET_NULL
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]

    class Meta:
        verbose_name = 'Usuario'

    def __str__(self):
        return self.username
