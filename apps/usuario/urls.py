from rest_framework.routers import DefaultRouter
from apps.usuario.views import UsuarioViewSet


router = DefaultRouter()
router.register(r'usuario',viewset=UsuarioViewSet, basename='usuario')


urlpatterns = router.urls
