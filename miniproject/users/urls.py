from django.urls import path 
from .views import user_registration, user_profile, CustomTokenObtainPairView, logout_view

urlpatterns = [ 
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('logout/', logout_view),
    path('registration/', user_registration, name='user_registration'),
    path('profile', user_profile, name='user_profile'),
] 