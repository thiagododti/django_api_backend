from django.db import transaction
from rest_framework import serializers

from . import PessoaFisicaSerializer, PessoaJuridicaSerializer
from ..models import Cliente, PessoaFisica, PessoaJuridica
from apps.cliente.validators.cpf_cnpj_validators import *


class ClienteSerializer(serializers.ModelSerializer):
    pf = PessoaFisicaSerializer(required=False,allow_null=True)
    pj = PessoaJuridicaSerializer(required=False,allow_null=True)

    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        tipo = data.get("TIPO") or getattr(self.instance, "TIPO", None)

        has_cpf = "cpf" in data and data["cpf"] is not None
        has_cnpj = "cnpj" in data and data["cnpj"] is not None

        if tipo == Cliente.TIPO_PF and not has_cpf and not getattr(self.instance, "pf", None):
            raise serializers.ValidationError({"pf": "Dados de Pessoa Física são necessários para tipo Pessoa Fisica."})
        if tipo == Cliente.TIPO_PJ and not has_cnpj and not getattr(self.instance, "pj", None):
            raise serializers.ValidationError({"pj": "Dados de Pessoa Jurídica são necessários para tipo Pessoa Jurídica."})
        if tipo not in (Cliente.TIPO_PF, Cliente.TIPO_PJ):
            raise serializers.ValidationError({"tipo": "Tipo inválido."})
        return data

    def create(self, validated_data):
        pf_data = validated_data.pop("cliente_pessoa_fisica",None)
        pj_data = validated_data.pop("cliente_pessoa_juridica",None)

        with transaction.atomic():
            cliente = Cliente.objects.create(**validated_data)
            if cliente.TIPO == Cliente.TIPO_PF and pf_data:
                PessoaFisica.objects.create(cliente=cliente, **pf_data)
            elif cliente.TIPO == Cliente.TIPO_PJ and pj_data:
                PessoaJuridica.objects.create(cliente=cliente, **pj_data)
        return cliente

    def update(self, instance, validated_data):
        pf_data = validated_data.pop("cliente_pessoa_fisica",None)
        pj_data = validated_data.pop("cliente_pessoa_juridica",None)

        with transaction.atomic():
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

            # tratar PF
            if instance.TIPO == Cliente.TIPO_PF:
                if pf_data:
                    pf_obj,created = PessoaFisica.objects.update_or_create(cliente=instance,defaults=pf_data)
                PessoaFisica.objects.filter(cliente=instance).delete()
            elif instance.TIPO == Cliente.TIPO_PJ:
                if pj_data:
                    pj_obj,created = PessoaJuridica.objects.update_or_create(cliente=instance,defaults=pj_data)
                PessoaJuridica.objects.filter(cliente=instance).delete()
        return instance

