from django.shortcuts import render
from .models import *

# Create your views here.

def resume_view(request):
    resume = ResumeUpload.objects.first()
    return render(request,'resume.html',{'resume':resume})

def project_view(request):
    projects = Project.objects.all().order_by('-created_to')
    return render(request, 'project.html', {'projects': projects})

def about_view(request):
    about = About.objects.first()  # assuming one profile
    skills = Skill.objects.all()
    certifications = Certification.objects.all()
    return render(request, 'about.html', {'about': about,'skills': skills,'certifications': certifications})

