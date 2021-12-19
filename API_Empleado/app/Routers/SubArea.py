from app.Views.SubArea import SubAreaViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'',SubAreaViewSet)
urlpatterns=router.urls