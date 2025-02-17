from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'technology/index.html', {'text':'TEC9'})
