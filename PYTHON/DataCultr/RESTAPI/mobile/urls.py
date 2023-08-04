from django.urls import include, path

from rest_framework import routers

from mobile.views import BrandViewSet, ModelViewSet

router = routers.DefaultRouter()
router.register(r'model', ModelViewSet)
router.register(r'brand', BrandViewSet)

urlpatterns = [
   path('', include(router.urls)),
]