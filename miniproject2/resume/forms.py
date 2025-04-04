from django import forms

class ResumeUploadForm(forms.Form):
    file = forms.FileField(label="Upload your resume (PDF or DOCX)")
