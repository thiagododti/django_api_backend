from rest_framework import serializers
from ..models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    foto = serializers.ImageField(
        required=False,
        allow_null=True
    )

    class Meta:
        model = Usuario
        fields = ['id',
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
                  'foto']

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
