import django_filters
from apps.cliente.models import Cliente

class ClienteFilterSet(django_filters.FilterSet):
    razao = django_filters.CharFilter(field_name='razao', lookup_expr='icontains')
    cpf_cnpj = django_filters.CharFilter(field_name='cpf_cnpj', lookup_expr='icontains')
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='icontains')
    class Meta:
        model = Cliente
        fields = ['razao_social','cpf_cnpj','tipo']