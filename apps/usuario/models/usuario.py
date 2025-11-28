from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    """
    Modelo personalizado de usuário que estende o AbstractUser do Django.
    Adiciona campos adicionais para armazenar informações específicas do usuário.
    """
    telefone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Telefone"
    )
    endereco = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Endereço"
    )
    data_nascimento = models.DateField(
        blank=True,
        null=True,
        verbose_name="Data de Nascimento"
    )
    foto = models.ImageField(
        upload_to='fotos_usuarios/',
        blank=True,
        null=True,
        verbose_name="Foto do Usuário"
    )

    class Meta:
        db_table = 'usuario'
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.username
