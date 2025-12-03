from rest_framework import serializers
from apps.cliente.models import PessoaJuridica


class PessoaJuridicaSerializer(serializers.Serializer):
    class Meta:
        model = PessoaJuridica
        fields = '__all__'
