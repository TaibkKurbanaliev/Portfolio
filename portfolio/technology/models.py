from django.db import models

class Technology(models.Model): 
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=512)
    description = models.TextField()
    technology_owner = models.ForeignKey(to=Technology, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.name} | {self.technology_owner.name}'
    
class ProjectImages(models.Model):
    image = models.ImageField(upload_to='project_images')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} image | {self.project.name}'