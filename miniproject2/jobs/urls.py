from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, JobRecommendationsView

router = DefaultRouter()
router.register(r'api', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('recommend/', JobRecommendationsView.as_view(), name='job-recommend'),

]
