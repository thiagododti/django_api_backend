from rest_framework import serializers
from apps.cliente.models import PessoaFisica


class PessoaFisicaSerializer(serializers.Serializer):
    class Meta:
        model = PessoaFisica
        fields = '__all__'
