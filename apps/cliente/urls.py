from rest_framework.routers import DefaultRouter
from apps.cliente.views import ClienteViewSet


router = DefaultRouter()

router.register(viewset=ClienteViewSet, basename='cliente', prefix='')

urlpatterns = router.urls