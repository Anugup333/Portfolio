from django.shortcuts import render
from .models import *

# Create your views here.

def resume_view(request):
    resume = ResumeUpload.objects.first()
    return render(request,'resume.html',{'resume':resume})

def project_view(request):
    projects = Project.objects.all().order_by('-created_to')
    return render(request, 'project.html', {'projects': projects})