import django_filters
from apps.usuario.models import Usuario


class UsuarioFilterSet(django_filters.FilterSet):
    username = django_filters.CharFilter(
        field_name='username', lookup_expr='icontains', label='Nome de usuário')
    email = django_filters.CharFilter(
        field_name='email', lookup_expr='icontains', label='E-mail')
    first_name = django_filters.CharFilter(
        field_name='first_name', lookup_expr='icontains', label='Nome')
    last_name = django_filters.CharFilter(
        field_name='last_name', lookup_expr='icontains', label='Sobrenome')

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name']
