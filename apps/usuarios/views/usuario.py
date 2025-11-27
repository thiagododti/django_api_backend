from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from ..models import Usuario
from ..serializers import UsuarioSerializer
from ..filter.usuario import UsuarioFilterSet
from drf_spectacular.utils import extend_schema


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


@extend_schema(
    tags=["Usuários"],  # esta será a seção/grupo no Swagger
    description="Operações de CRUD para usuários."
)
class UsuarioViewSet(PermissionsMixin):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = UsuarioFilterSet
