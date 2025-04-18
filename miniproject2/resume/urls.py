from django.urls import path
from .views import upload_resume, resume_detail
from jobs.views import JobRecommendationsView
urlpatterns = [
    path('upload/', upload_resume, name="upload_resume"),
    path('<str:resume_id>/', resume_detail, name="resume_detail"),
    path('<str:resume_id>/recommends', JobRecommendationsView.as_view(), name="recommends"),
]
