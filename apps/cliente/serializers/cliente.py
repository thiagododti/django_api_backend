from django.db import transaction
from rest_framework import serializers

from apps.cliente.serializers.pessoa_fisica import PessoaFisicaSerializer
from apps.cliente.serializers.pessoa_juridica import PessoaJuridicaSerializer
from ..models import Cliente, PessoaFisica, PessoaJuridica
from apps.cliente.validators.cpf_cnpj_validators import *


class ClienteSerializer(serializers.ModelSerializer):

    # Mapeia explicitamente os relacionamentos OneToOne pelos related_name dos models
    pessoa_fisica = PessoaFisicaSerializer(required=False)
    pessoa_juridica = PessoaJuridicaSerializer(required=False)

    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ['data_criacao']

    def validate(self, data):
        tipo = data.get('tipo')
        # Como os campos não usam source customizado, eles entram com o nome do field
        pessoa_fisica = data.get('pessoa_fisica')
        pessoa_juridica = data.get('pessoa_juridica')

        if tipo == 'cpf' and not pessoa_fisica:
            raise serializers.ValidationError(
                "Dados de Pessoa Física são obrigatórios para o tipo 'cpf'.")

        if tipo == 'cnpj' and not pessoa_juridica:
            raise serializers.ValidationError(
                "Dados de Pessoa Jurídica são obrigatórios para o tipo 'cnpj'.")

        return data

    def create(self, validated_data):
        # Dados aninhados entram com o nome do field em validated_data
        pessoa_fisica_data = validated_data.pop('pessoa_fisica', None)
        pessoa_juridica_data = validated_data.pop('pessoa_juridica', None)

        with transaction.atomic():
            cliente = Cliente.objects.create(**validated_data)

            if pessoa_fisica_data:
                PessoaFisica.objects.create(
                    cliente=cliente, **pessoa_fisica_data)

            if pessoa_juridica_data:
                PessoaJuridica.objects.create(
                    cliente=cliente, **pessoa_juridica_data)

        return cliente

    def update(self, instance, validated_data):
        pessoa_fisica_data = validated_data.pop('pessoa_fisica', None)
        pessoa_juridica_data = validated_data.pop('pessoa_juridica', None)
        with transaction.atomic():
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

            if pessoa_fisica_data:
                pessoa_fisica, _ = PessoaFisica.objects.get_or_create(
                    cliente=instance)
                for attr, value in pessoa_fisica_data.items():
                    setattr(pessoa_fisica, attr, value)
                pessoa_fisica.save()

            if pessoa_juridica_data:
                pessoa_juridica, _ = PessoaJuridica.objects.get_or_create(
                    cliente=instance)
                for attr, value in pessoa_juridica_data.items():
                    setattr(pessoa_juridica, attr, value)
                pessoa_juridica.save()

        return instance
