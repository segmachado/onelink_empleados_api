from app.Views.Empleado import EmpleadoViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'',EmpleadoViewSet)
urlpatterns=router.urls