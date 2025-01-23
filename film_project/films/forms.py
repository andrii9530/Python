from django import forms
from .models import Film, Genre

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'release_year', 'rating', 'image_url', 'trailer_url', 'genres']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'genres': forms.CheckboxSelectMultiple(),  # Відображення жанрів як чекбокси
        }
