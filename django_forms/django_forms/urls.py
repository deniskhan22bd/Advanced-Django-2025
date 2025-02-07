from django.urls import path 

from django.contrib import admin
from forms.views import contact_view, success_view 

 

urlpatterns = [ 
    path('admin/', admin.site.urls),

    path('contact/', contact_view, name='contact'),  
    path('success/', success_view, name='success_page'),


] 

