from django.shortcuts import render
#from django.http import HttpResponse
from .models import Project

# Create your views here.
def hme(request):
  all_projects = Project.objects.all()  # get all data for projects from the database
  return render(request, 'portfolio/home.html', {'projects': all_projects})