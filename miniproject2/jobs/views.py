from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from jobs.models import Job
from resume.models import Resume
from .serializers import JobSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from resume.utils import ai_chat
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = []
    authentication_classes = []

class JobRecommendationsView(APIView):
    permission_classes = []
    authentication_classes = []
    def get(self, request, resume_id):
        resume = get_object_or_404(Resume, id=resume_id)
        jobs = Job.objects.all()
        jobs_data = [
            {
                "id": job.id,
                "title": job.title,
                "company": job.company,
                "required_skills": job.required_skills,
                "required_experience": job.required_experience,
                "location": job.location,
                "is_remote": job.is_remote,
            }
            for job in jobs
        ]
        prompt = f"""
        You are a recruiter‑assistant AI. A candidate has the following resume:
        {resume.parsed_data}

        Below is the list of open jobs in our system (JSON array).  
        Choose the 3 most suitable jobs for this candidate based on skills, experience, and location.  
        Jobs:
        {jobs_data}
        Return a ONLY JSON array of objects {{ "job_id": <id>, "score": <0–100> }} sorted by score descending.
        """
        
        res = ai_chat(prompt)
        result = []
        for rec in res:
            job = Job.objects.filter(id=(rec["job_id"])).first()
            if not job:
                continue
            serializer = JobSerializer(job)
            result.append({
                "job": serializer.data,
                "score": rec["score"]
            })
        return Response(result, status=status.HTTP_200_OK) 