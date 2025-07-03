from django.shortcuts import render
from .models import Project
# Create your views here.

def project_list(request):
    project = Project.objects.all()
    context={"projects": project}
    return render(request, "content/project_list.html", context)