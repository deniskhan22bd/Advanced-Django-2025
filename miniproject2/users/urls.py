from django.urls import path 
from .views import CustomTokenObtainPairView, ExampleView, CustomTokenRefreshView, logout, register, reset_password, CustomRegisterView

urlpatterns = [ 
    path('token/', CustomTokenObtainPairView.as_view(),name='token'), 
    path('token/refresh/', CustomTokenRefreshView.as_view(),name='token-refresh'), 
    path('logout/', logout, name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('reset/', reset_password, name='reset_password'),
    path('test/', ExampleView.as_view(), name="test")
] 