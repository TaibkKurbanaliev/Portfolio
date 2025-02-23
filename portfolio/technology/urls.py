from django.urls import path

from technology.views import index

app_name = 'technology'

urlpatterns = [
    path('', index, name='index'),
]