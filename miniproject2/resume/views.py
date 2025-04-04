import os
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ResumeUploadForm
from .models import Resume
from .utils import parse_resume
# Create your views here.
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

            return redirect("resume_detail", resume_id=resume_instance.id)
    else:
        form = ResumeUploadForm()
    return render(request, "resume/upload.html", {"form": form})

def resume_detail(request, resume_id):
    resume_instance = Resume.objects.get(id=resume_id)
    # print(resume_instance.parsed_data)
    return render(request, "resume/detail.html", {"resume": resume_instance})

