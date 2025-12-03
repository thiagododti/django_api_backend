from django.db import models


class Departamento(models.Model):
    NOME = models.CharField(
        max_length=100,
        verbose_name='Departamento'
    )
    STATUS = models.BooleanField(
        default=True,
        verbose_name='Status'
    )
    DESCRICAO = models.TextField(
        verbose_name='Descricao'
    )
    DATA_CRIACAO = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    DATA_ATUALIZACAO = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização'

    )
    DEPARTAMENTO_PAI = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='departamento_pai',
        verbose_name='Departamento Pai')

    def __str__(self):
        return self.NOME

    class Meta:
        db_table = 'DEPARTAMENTO'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['NOME']
