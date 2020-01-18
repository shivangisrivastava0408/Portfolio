from django.shortcuts import render
from projects.models import Project
# Create your views here.

def project_index(request):
    return render(request, 'project_index.html', {})

def myself(request):
    return render(request, 'myself.html', {})

def about(request):
    return render(request, 'about.html', {})

def qualifications(request):
    return render(request, 'qualifications.html', {})

def skills(request):
    return render(request, 'skills.html', {})

def experience(request):
    return render(request, 'experience.html', {})