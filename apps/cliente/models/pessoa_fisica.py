import re

from django.db import models
from django.forms import ValidationError
from apps.cliente.models import Cliente


class PessoaFisica(models.Model):
    CLIENTE = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='cliente_pessoa_fisica'
    )
    NOME = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )
    CPF = models.CharField(
        max_length=11,
        blank=False,
        null=False,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.CLIENTE.TIPO:
            self.CLIENTE.TIPO = 'cpf'
            self.CLIENTE.save()
            super().save(*args, **kwargs)

    def validate_cpf(self):
        cpf = re.sub(r'\D', '', self.CPF)
        if len(cpf) != 11:
            raise ValidationError("CPF deve conter 11 dígitos.")

        if cpf == cpf[0] * len(cpf):
            raise ValidationError("CPF inválido.")

        def calc_digit(digs):
            s = sum(int(d)*w for d, w in zip(digs, range(len(digs)+1, 1, -1)))
            r = (s * 10) % 11
            return '0' if r == 10 else str(r)
        d1 = calc_digit(cpf[:9])
        d2 = calc_digit(cpf[:9] + d1)
        if cpf[-2:] != d1 + d2:
            raise ValidationError("CPF inválido.")

    def __str__(self):
        return self.NOME

    class Meta:
        db_table = 'PESSOA_FISICA'
        verbose_name = "Pessoa Fisica"
        verbose_name_plural = "Pessoas Fisica"
        ordering = ['NOME']
