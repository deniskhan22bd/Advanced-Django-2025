from django.urls import path 
from .views import user_registration, UserProfileView, CustomTokenObtainPairView, logout_view

urlpatterns = [ 
    path('login/', CustomTokenObtainPairView.as_view(),name='login'), 
    path('logout/', logout_view),
    path('registration/', user_registration, name='registration'),
    path('profile/', UserProfileView.as_view(), name='profile'),
] 