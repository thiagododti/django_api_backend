import re

from django.db import models
from django.forms import ValidationError
from apps.cliente.models import Cliente
from apps.cliente.validators.cpf_cnpj_validators import validate_cpf


class PessoaFisica(models.Model):
    CLIENTE = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='cliente_pessoa_fisica'
    )
    NOME = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        verbose_name="Nome"
    )
    CPF = models.CharField(
        max_length=11,
        blank=False,
        null=False,
        unique=True,
        validators=[validate_cpf],
        verbose_name="CPF"
    )

    def save(self, *args, **kwargs):
        # Garante consistência do tipo do cliente
        if not self.CLIENTE.TIPO:
            self.CLIENTE.TIPO = 'cpf'
            self.CLIENTE.save()
        elif self.CLIENTE.TIPO != 'cpf':
            # Mantém coerência caso o tipo esteja diferente
            self.CLIENTE.TIPO = 'cpf'
            self.CLIENTE.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.NOME

    class Meta:
        db_table = 'PESSOA_FISICA'
        verbose_name = "Pessoa Fisica"
        verbose_name_plural = "Pessoas Fisica"
        ordering = ['NOME']
