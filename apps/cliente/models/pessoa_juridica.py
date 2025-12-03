import re
from django.db import models
from django.forms import ValidationError
from apps.cliente.models import Cliente


class PessoaJuridica(models.Model):
    CLIENTE = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='cliente_pessoa_juridica'
    )
    RAZAO_SOCIAL = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )
    CNPJ = models.CharField(
        max_length=18,
        blank=False,
        null=False,
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.CLIENTE.TIPO:
            self.CLIENTE.TIPO = 'cnpj'
            self.CLIENTE.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.RAZAO_SOCIAL

    def validate_cnpj(self):
        cnpj = re.sub(r'\D', '', self.CNPJ)
        if len(cnpj) != 14:
            raise ValidationError("CNPJ deve ter 14 dígitos.")
        if cnpj == cnpj[0] * 14:
            raise ValidationError("CNPJ inválido.")

        def calc_digit(digs, weights):
            s = sum(int(d) * w for d, w in zip(digs, weights))
            r = s % 11
            return '0' if r < 2 else str(11 - r)
        weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        weights2 = [6] + weights1
        d1 = calc_digit(cnpj[:12], weights1)
        d2 = calc_digit(cnpj[:12] + d1, weights2)
        if cnpj[-2:] != d1 + d2:
            raise ValidationError("CNPJ inválido.")

    class Meta:
        db_table = 'PESSOA_JURIDICA'
        verbose_name = "Pessoa Juridica"
        verbose_name_plural = "Pessoas Juridica"
        ordering = ['RAZAO_SOCIAL']
