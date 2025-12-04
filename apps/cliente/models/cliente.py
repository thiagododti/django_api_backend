from django.db import models


# Create your models here.
class Cliente(models.Model):
    TIPO_PF = "cpf"
    TIPO_PJ = "cnpj"
    tipo_choices = (
        (TIPO_PJ, 'Pessoa Juridica'),
        (TIPO_PF, 'Pessoa Fisica'),
    )

    # Colunas ####
    tipo = models.CharField(
        max_length=10,
        choices=tipo_choices
    )
    email = models.EmailField(
        unique=True,
        blank=True,
        null=True
    )
    data_criacao = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'cliente'
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['data_criacao']
