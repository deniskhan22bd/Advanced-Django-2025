from django.contrib import admin 
from django.urls import path, include 
from users.views import CustomTokenObtainPairView, logout_view
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('logout/', logout_view)
] 