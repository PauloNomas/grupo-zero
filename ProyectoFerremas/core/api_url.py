# core/api_urls.py
from rest_framework.routers import DefaultRouter
from .api_views import ProductoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = router.urls