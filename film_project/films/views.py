from django.shortcuts import render, get_object_or_404
from .models import Film
# Create your views here

def film_list(reguest):
    films = Film.objects.all()
    return render(reguest, 'films/film_list.html', {'films':films})

def film_detail(reguest,pk):
    film = get_object_or_404(Film, pk=pk)
    return render(reguest, 'films/film_detail.html', {'film':film})
