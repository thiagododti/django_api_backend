from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Usuario
from ..serializers import UsuarioSerializer, UsuarioAutenticadoSerializer
from ..filter.usuario import UsuarioFilterSet
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.authentication import JWTAuthentication


@extend_schema(
    tags=["Usuario"],  # esta será a seção/grupo no Swagger
    description="Operações de CRUD para usuários."
)
class PermissionsUsuarioMixin(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
):
    pass


class UsuarioViewSet(PermissionsUsuarioMixin):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]
    # opcional, se você usar TokenAuth
    authentication_classes = [JWTAuthentication]
    filterset_class = UsuarioFilterSet

    @extend_schema(
        summary="Obter dados do usuário autenticado",
        description="Retorna os dados completos do usuário que está fazendo a requisição autenticada.",
        responses={200: UsuarioAutenticadoSerializer}
    )
    @action(detail=False, methods=['get'], url_path='autenticado')
    def get_authenticated_user(self, request):
        """
        Endpoint para obter os dados do usuário autenticado.

        Esta view retorna as informações do usuário que está fazendo a requisição,
        baseado no token de autenticação fornecido.
        """
        serializer = UsuarioAutenticadoSerializer(request.user)
        return Response(serializer.data)
