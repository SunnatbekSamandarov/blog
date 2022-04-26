from django.db import models

# Create your models here.
class Post(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Subject = models.CharField(max_length=200)
    Message = models.TextField()

    def __str__(self):
        return self.Name