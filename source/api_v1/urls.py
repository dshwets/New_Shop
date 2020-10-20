from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_v1.views import ProductViewSet, OrderApi

router = DefaultRouter()
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/<int:pk>/', OrderApi.as_view(), name='order_api'),
]