from django.urls import path 

from django.contrib import admin
from forms.views import contact_view, success_view, create_cv, cv_list

from django.conf import settings 
from django.conf.urls.static import static 
 

urlpatterns = [ 
    path('admin/', admin.site.urls),

    path('contact/', contact_view, name='contact'),  
    path('success/', success_view, name='success_page'),
    path('create/', create_cv, name='create_cv'),
    path('cv_list/', cv_list, name='cv_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

