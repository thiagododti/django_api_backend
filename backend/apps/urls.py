from django.urls import path, include

urlpatterns = [
    path('usuario/', include('apps.usuario.urls')),
    path('cliente/', include('apps.cliente.urls')),
]
