from app.views import DocumentoViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'',DocumentoViewSet)
urlpatterns=router.urls