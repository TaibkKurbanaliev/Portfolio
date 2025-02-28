from django.urls import path

from technology.views import technology_add, technology_del, project_add, project_del, image_add

app_name = 'technology'

urlpatterns = [
    path('add/', technology_add, name='technology_add'),
    path('del/<int:id>/', technology_del, name='technology_del'),
    path('projects/add/<int:id>/', project_add, name='project_add'),
    path('projects/del/<int:id>/', project_del, name='project_del'),
    path('images/add/<int:id>/', image_add, name='image_add')
]