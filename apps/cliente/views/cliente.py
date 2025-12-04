from rest_framework import (viewsets, mixins)
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.cliente.models import Cliente
from apps.cliente.serializers import ClienteSerializer
from apps.cliente.filters import ClienteFilterSet


@extend_schema(
    tags=['Cliente'],
    description="Operações de CRUD para clientes."
)
class PermissionsClienteMixin(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
):
    pass


class ClienteViewSet(PermissionsClienteMixin):
    queryset = Cliente.objects.select_related(
        'pessoa_fisica', 'pessoa_juridica')
    permission_classes = [IsAuthenticated]
    serializer_class = ClienteSerializer
    filterset_class = ClienteFilterSet
