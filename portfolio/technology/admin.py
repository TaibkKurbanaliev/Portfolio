from django.contrib import admin

# Register your models here.
from technology.models import Technology, Project, ProjectImages

admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(ProjectImages)