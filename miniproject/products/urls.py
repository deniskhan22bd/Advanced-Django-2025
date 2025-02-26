from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, TagViewSet, ProductListView 

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('api/', include(router.urls)),
]
