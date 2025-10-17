from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from ..models import Usuario
from ..serializers import UsuarioSerializer


class PermissionsMixin(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    """
    Mixin de permissões para o ViewSet de Usuários.
    Contém as operações de listagem, criação, recuperação e atualização.

    # Inherits:
        - viewsets.GenericViewSet: Fornece a funcionalidade básica de ViewSet.
        - mixins.ListModelMixin: Permite listar objetos.
        - mixins.CreateModelMixin: Permite criar novos objetos.
        - mixins.RetrieveModelMixin: Permite recuperar um objeto específico.
        - mixins.UpdateModelMixin: Permite atualizar um objeto existente.
        - mixins.DestroyModelMixin: Permite deletar um objeto existente. -- Removido.
    """
    pass


class UsuarioViewSet(PermissionsMixin):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]
