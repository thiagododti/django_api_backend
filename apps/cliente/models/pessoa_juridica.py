import re
from django.db import models
from django.forms import ValidationError
from apps.cliente.models import Cliente
from apps.cliente.validators.cpf_cnpj_validators import validate_cnpj


class PessoaJuridica(models.Model):
    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='pessoa_juridica'
    )
    razao_social = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        verbose_name="Razão Social"
    )
    cnpj = models.CharField(
        max_length=18,
        blank=False,
        null=False,
        unique=True,
        validators=[validate_cnpj],
        verbose_name="CNPJ"
    )

    def save(self, *args, **kwargs):
        if not self.cliente.tipo:
            self.cliente.tipo = 'cnpj'
            self.cliente.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.razao_social

    class Meta:
        db_table = 'pessoa_juridica'
        verbose_name = "Pessoa Juridica"
        verbose_name_plural = "Pessoas Juridica"
        ordering = ['razao_social']
