from rest_framework import serializers
from apps.cliente.models import PessoaFisica


class PessoaFisicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaFisica
        fields = ['NOME', 'CPF']
