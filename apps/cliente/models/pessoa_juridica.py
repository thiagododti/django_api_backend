import re
from django.db import models
from django.forms import ValidationError
from apps.cliente.models import Cliente
from apps.cliente.validators.cpf_cnpj_validators import validate_cnpj


class PessoaJuridica(models.Model):
    CLIENTE = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='cliente_pessoa_juridica'
    )
    RAZAO_SOCIAL = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        verbose_name="Razão Social"
    )
    CNPJ = models.CharField(
        max_length=18,
        blank=False,
        null=False,
        unique=True,
        validators=[validate_cnpj],
        verbose_name="CNPJ"
    )

    def save(self, *args, **kwargs):
        if not self.CLIENTE.TIPO:
            self.CLIENTE.TIPO = 'cnpj'
            self.CLIENTE.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.RAZAO_SOCIAL

    class Meta:
        db_table = 'PESSOA_JURIDICA'
        verbose_name = "Pessoa Juridica"
        verbose_name_plural = "Pessoas Juridica"
        ordering = ['RAZAO_SOCIAL']
