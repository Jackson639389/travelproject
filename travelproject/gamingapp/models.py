from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
class team(models.Model):
    name = models.CharField(max_length=220)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
