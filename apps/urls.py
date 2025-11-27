from django.urls import path, include

urlpatterns = [
    path('usuarios/', include('apps.usuarios.urls')),
]
