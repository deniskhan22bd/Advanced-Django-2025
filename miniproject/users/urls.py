from django.urls import path 
from .views import user_registration, UserProfileView, CustomTokenObtainPairView, logout_view
from django.contrib.auth import views as auth_views 

urlpatterns = [ 
    path('login/', CustomTokenObtainPairView.as_view(),name='login'), 
    path("logout/", logout_view, name="logout"), 
    path('registration/', user_registration, name='registration'),
    path('profile/', UserProfileView.as_view(), name='profile'),
] 