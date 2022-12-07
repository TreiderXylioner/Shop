from django.db import models

# Create your models here.

class Woman_clothes(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title
