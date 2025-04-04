from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to="services/", default="service.jpg")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Services"
    
    def __str__(self) -> str:
        return self.name
    

class Project(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    description = models.TextField()
    client = models.CharField(max_length=100)
    address = models.CharField(max_length=1024)
    location = models.CharField(max_length=1024)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Use slugify for consistent slug format
        super(Project, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Projects"

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/', default="project_image.jpg")

    def __str__(self) -> str:
        return f"Image for {self.project.title}"
