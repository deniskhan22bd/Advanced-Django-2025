import os
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ResumeUploadForm
from .models import Resume
from .utils import parse_resume
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.permissions import AllowAny

@authentication_classes([])
def upload_resume(request):
    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            resume_instance = Resume(file=uploaded_file)
            resume_instance.save()
            file_path = os.path.join(settings.MEDIA_ROOT, resume_instance.file.name)
            parsed_data = parse_resume(file_path)
            resume_instance.parsed_data = parsed_data
            resume_instance.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'id': resume_instance.id})
            else:
                return redirect("resume_detail", resume_id=resume_instance.id)
    else:
        form = ResumeUploadForm()
    return render(request, "resume/upload.html", {"form": form})

@authentication_classes([])
@api_view(['GET',])
def resume_detail(request, resume_id):
    resume_instance = get_object_or_404(Resume, id=resume_id)
    parsed = resume_instance.parsed_data
    return Response({
        "id": resume_instance.id,
        "file": resume_instance.file.url if resume_instance.file else None,
        "parsed_data": {
            "name": parsed.get("name", ""),
            "email": parsed.get("email", ""),
            "experience": parsed.get("experience", []),
            "skills": parsed.get("skills", []),
            "education": parsed.get("education", []),
            "feedback": parsed.get("feedback", ""),
            "suggestions": parsed.get("suggestions", "")
        }
    })


