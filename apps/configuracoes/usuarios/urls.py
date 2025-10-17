from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

router = DefaultRouter()
router.register(viewset=UsuarioViewSet, basename='usuarios', prefix='')

urlpatterns = router.urls
