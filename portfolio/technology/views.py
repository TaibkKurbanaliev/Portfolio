from django.shortcuts import render, HttpResponse
from technology.models import Project, ProjectImages, Technology

def index(request):
    technologies = Technology.objects.all()
    projects = list()
    for index, technology in enumerate(technologies):
        projects.append(Project.objects.filter(technology_owner=technology.id))
    
    tech_projects = zip(technologies, projects)
    
    print(projects)
    context = {
        'title' : 'Portfolio',
        'tech_projects': tech_projects,
        'ProjectImages' : ProjectImages.objects.all(),
    }
    
    return render(request, 'technology/index.html', context)
