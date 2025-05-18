from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'personal_portfolio/home.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'personal_portfolio/projects.html', {'projects': projects})

def contact(request):
    return render(request, 'personal_portfolio/contact.html')