from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    trailer_url = models.URLField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='films')

    def __str__(self):
        return self.title
    

