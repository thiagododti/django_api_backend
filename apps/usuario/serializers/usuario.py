from rest_framework import serializers
from ..models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    foto = serializers.ImageField(
        required=False,
        allow_null=True
    )
    password = serializers.CharField(
        write_only=True,
        required=False,  # ⬅️ nunca obrigatório por padrão
        min_length=8,
        style={'input_type': 'password'}
    )

    class Meta:
        model = Usuario
        fields = [
            'id',
            'last_login',
            'is_superuser',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
            'telefone',
            'endereco',
            'data_nascimento',
            'foto'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            # Atualização: senha não é obrigatória
            self.fields['password'].required = False
        else:
            # Criação: senha é obrigatória
            self.fields['password'].required = True

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)  # 🔐 hash correto
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

    def validate_foto(self, value):
        max_size = 2 * 1024 * 1024  # 2MB
        if value.size > max_size:
            raise serializers.ValidationError(
                "A imagem não pode ser maior que 2MB."
            )
        return value


class UsuarioReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['password']
