from django.db import models

class Technology(models.Model): 
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(null=True, blank=True)

class Project(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=512)
    imdage = models.ImageField(upload_to='project_iamges')
    description = models.TextField()
    technology_owner = models.ForeignKey(to=Technology, on_delete=models.PROTECT)