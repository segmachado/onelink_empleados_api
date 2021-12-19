from app.Views.Area import AreaViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'',AreaViewSet)
urlpatterns=router.urls