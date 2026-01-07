from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Usuario
from ..serializers import UsuarioSerializer, UsuarioReadSerializer
from ..filter.usuario import UsuarioFilterSet
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser


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
    parser_classes = [MultiPartParser]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UsuarioReadSerializer
        return UsuarioSerializer
