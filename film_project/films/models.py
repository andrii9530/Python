from django.db import models

# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1) 
    genres = models.ManyToManyField('Genre', related_name='films')

    def __str__(self):
        return self.title
    
class Ganre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

