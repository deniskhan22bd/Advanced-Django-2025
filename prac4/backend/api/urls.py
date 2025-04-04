from django.urls import path, include 

from rest_framework.routers import DefaultRouter 

from .views import ItemViewSet, RegisterView

 

router = DefaultRouter() 

router.register(r'items', ItemViewSet) 

 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
 
urlpatterns = [ 

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 

    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'), 

    path('', include(router.urls)), 

] 

urlpatterns += [ 

    path('register/', RegisterView.as_view(), name='register'), 

] 

 