from django.db import models
from django.contrib.auth.models import AbstractUser


# Modelo para gestión de usuarios en Django y SQLite
class CregevalUSer(AbstractUser):

    email = models.EmailField(
        verbose_name='Correo electrónico',
        help_text='Ingrese el correo electrónico de la cuenta para el cliente',
        unique=True
    )

    first_name = models.CharField(
        verbose_name='Nombre del cliente',
        help_text='Indique el nombre del cliente',
        max_length=100
    )

    last_name = models.CharField(
        verbose_name='Apellido del cliente',
        help_text='Indique el apellido del cliente',
        max_length=100
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
