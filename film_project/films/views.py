from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, Genre
from django.http import HttpResponse
from .forms import FilmForm
import os
from django.conf import settings

def film_list(request):
    genre_filter = request.GET.get('genre', '')  
    genres = Genre.objects.all()  
    films = Film.objects.all()  
    
    if genre_filter:
        films = films.filter(genres__id=genre_filter)

    return render(request, 'films/film_list.html', {'films': films, 'genres': genres, 'request': request})

# Деталі фільму
def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'films/film_detail.html', {'film': film})

def admin_dashboard(request):
    films = Film.objects.prefetch_related('genres').all()
    return render(request, 'admin/admin_dashboard.html', {'films': films})

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FilmForm()
    return render(request, 'admin/add_film.html', {'form': form})

def edit_film(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FilmForm(instance=film)
    return render(request, 'admin/edit_film.html', {'form': form, 'film': film})

def delete_film(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    if request.method == 'POST':
        film.delete()
        return redirect('admin_dashboard')
    return render(request, 'admin/delete_film.html', {'film': film})
