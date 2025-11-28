from rest_framework.routers import DefaultRouter
from apps.usuario.views import UsuarioViewSet


router = DefaultRouter()
router.register(basename='usuario', prefix='', viewset=UsuarioViewSet)


urlpatterns = router.urls
