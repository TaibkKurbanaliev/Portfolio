from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.urls import reverse
from technology.models import Project, ProjectImages, Technology

def technology_add(request):
    name = request.POST.get('technology_name')
    if name:
        Technology.objects.create(name=name, owner=request.user)
    return HttpResponseRedirect(reverse('users:profile_change'))

def technology_del(request, id):
    technology = Technology.objects.get(id=id)
    technology.delete()
    return HttpResponseRedirect(reverse('users:profile_change'))

def project_add(request, id):
    technology = get_object_or_404(Technology, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        link = request.POST.get('link')
        description = request.POST.get('description')
        print(f"{name} {description} {link}")
        if name and link and description:
            Project.objects.create(
                name=name,
                link=link,
                description=description,
                technology_owner=technology
            )
    
    return HttpResponseRedirect(reverse('users:profile_change'))

def project_del(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return HttpResponseRedirect(reverse('users:profile_change'))

def image_add(request, id):
    print(id)
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            project = get_object_or_404(Project, id=id)
            ProjectImages.objects.create(image=image, project=project)
    return HttpResponseRedirect(reverse('users:profile_change'))