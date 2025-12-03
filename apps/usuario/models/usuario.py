from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    """
    Modelo personalizado de usuário que estende o AbstractUser do Django.
    Adiciona campos adicionais para armazenar informações específicas do usuário.
    """
    TELEFONE = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Telefone"
    )
    ENDERECO = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Endereço"
    )
    DATA_NASCIMENTO = models.DateField(
        blank=True,
        null=True,
        verbose_name="Data de Nascimento"
    )
    FOTO = models.ImageField(
        upload_to='fotos_usuarios/',
        blank=True,
        null=True,
        verbose_name="Foto do Usuário"
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'USUARIO'
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['first_name', 'last_name']
