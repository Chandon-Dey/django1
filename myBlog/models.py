from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100, default='post Title')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
    thumbnail = models.ImageField(upload_to='cphotos/photos')