from django.shortcuts import render, redirect 

from .forms import ContactForm 

 

def contact_view(request): 

    if request.method == "POST": 

        form = ContactForm(request.POST) 

        if form.is_valid(): 

            form.save()  # Saves directly to the database 
            return redirect('success_page') 
    else: 
        form = ContactForm() 
    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, "success.html") 

from django.shortcuts import render, redirect 

from .forms import CVForm 

from .models import CV 

 

def create_cv(request): 

    if request.method == "POST": 

        form = CVForm(request.POST, request.FILES)  # Handle file uploads 

        if form.is_valid(): 

            form.save() 

            return redirect('cv_list')  # Redirect to CV listing page 

    else: 

        form = CVForm() 

    return render(request, 'cv_form.html', {'form': form}) 

def cv_list(request):
    CVs = CV.objects.all()
    return render(request, "cv_list.html",{"cvs": CVs})