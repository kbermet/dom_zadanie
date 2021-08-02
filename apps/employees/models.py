from django.db import models
from django.urls import reverse

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField()
    img = models.ImageField(upload_to='employees_images', null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('employees_detail_url', kwargs={'pk':self.pk})





