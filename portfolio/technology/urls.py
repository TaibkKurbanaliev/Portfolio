from django.urls import path

from technology.views import technology_add, project_add

app_name = 'technology'

urlpatterns = [
    path('add/<int:user_id>/', technology_add, name='technology_add'),
    path('projects/add/<int:product_id>/', project_add, name='prject_add'),
]