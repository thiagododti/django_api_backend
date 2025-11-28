from django.db import models

tipo_choices = (
    ('cnpj', 'Pessoa Juridica'),
    ('cpf', 'Pessoa Fisica'),
)


# Create your models here.
class Cliente(models.Model):
    razao_social = models.CharField(
        max_length=250
    )
    cpf_cnpj = models.CharField(
        max_length=14
    )
    tipo = models.CharField(
        max_length=10,
        choices=tipo_choices
    )

    def __str__(self):
        return self.razao_social

    class Meta:
        db_table = 'cliente'
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['razao_social']
