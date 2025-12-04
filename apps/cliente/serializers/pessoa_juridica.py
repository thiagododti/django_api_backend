from rest_framework import serializers
from apps.cliente.models import PessoaJuridica


class PessoaJuridicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaJuridica
        fields = ['razao_social', 'cnpj']
