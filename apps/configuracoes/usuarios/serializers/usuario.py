from rest_framework import serializers
from ..models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email',
                  'is_staff', 'is_active', 'date_joined', 'telefone', 'endereco', 'data_nascimento',
                  'foto', 'groups', 'user_permissions']
