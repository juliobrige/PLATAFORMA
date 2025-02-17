from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.username