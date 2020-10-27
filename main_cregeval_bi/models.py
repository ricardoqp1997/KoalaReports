from django.db import models


# Aquí se designaran los privilegios y sus tipos existentes en el portal, para accesos y prioridades
class CregevalCastType(models.Model):

    privilegio = models.CharField(
        verbose_name='Nombre del cargo o privilegio',
        help_text='En este campo se colocará el nombre del rango existente en el portal',
        max_length=100,
        unique=True
    )

    REQUIRED_FIELD = [
        'privilegio'
    ]

    class Meta:
        verbose_name = 'Privilegio'

    def __str__(self):
        return self.privilegio

    @property
    def get_privilegio(self):
        return self.privilegio
