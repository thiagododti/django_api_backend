from rest_framework import serializers
from ..models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email',
                  'is_staff', 'is_active', 'date_joined', 'telefone', 'endereco', 'data_nascimento',
                  'foto']
        read_only_fields = ['id', 'last_login',
                            'is_superuser', 'date_joined', 'username', 'email']


class UsuarioMeSerializer(serializers.ModelSerializer):
    """
    Serializer específico para o endpoint 'me' que retorna dados do usuário autenticado.
    Inclui apenas os campos mais relevantes para o frontend após o login.
    """
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'telefone',
                  'endereco', 'data_nascimento', 'foto', 'is_staff', 'is_active', 'last_login']
        read_only_fields = ['id', 'username', 'email',
                            'is_staff', 'is_active', 'last_login']
