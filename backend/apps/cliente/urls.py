from rest_framework.routers import DefaultRouter
from apps.cliente.views import ClienteViewSet


router = DefaultRouter()

router.register(basename='cliente', prefix='', viewset=ClienteViewSet)

urlpatterns = router.urls
