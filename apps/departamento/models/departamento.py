from django.db import models


class Departamento(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name='Departamento'
    )
    status = models.BooleanField(
        default=True,
        verbose_name='Status'
    )
    descricao = models.TextField(
        verbose_name='Descricao'
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização'

    )
    departamento_pai = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subdepartamentos',
        verbose_name='Departamento Pai')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'departamento'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['nome']
