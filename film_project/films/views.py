from django.shortcuts import render, get_object_or_404
from .models import Film, Genre

def film_list(request):
    genre_filter = request.GET.get('genre', '')  
    genres = Genre.objects.all()  
    films = Film.objects.all()  
    
    if genre_filter:
        films = films.filter(genres__id=genre_filter)

    return render(request, 'films/film_list.html', {'films': films, 'genres': genres, 'request': request})



def film_detail(reguest,pk):
    film = get_object_or_404(Film, pk=pk)
    return render(reguest, 'films/film_detail.html', {'film':film})
    
