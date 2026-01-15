import re

from django.db import models
from django.forms import ValidationError
from apps.cliente.models import Cliente
from apps.cliente.validators.cpf_cnpj_validators import validate_cpf


class PessoaFisica(models.Model):
    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='pessoa_fisica'
    )
    nome = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        verbose_name="Nome"
    )
    cpf = models.CharField(
        max_length=11,
        blank=False,
        null=False,
        unique=True,
        validators=[validate_cpf],
        verbose_name="CPF"
    )

    def save(self, *args, **kwargs):
        # Garante consistência do tipo do cliente
        if not self.cliente.tipo:
            self.cliente.tipo = 'cpf'
            self.cliente.save()
        elif self.cliente.tipo != 'cpf':
            # Mantém coerência caso o tipo esteja diferente
            self.cliente.tipo = 'cpf'
            self.cliente.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'pessoa_fisica'
        verbose_name = "Pessoa Fisica"
        verbose_name_plural = "Pessoas Fisica"
        ordering = ['nome']
