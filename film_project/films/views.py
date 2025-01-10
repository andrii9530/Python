from django.shortcuts import render
from .models import Film
# Create your views here

def film_list(reguest):
    films = Film.objects.all()
    return render(reguest, 'films/film_list.html', {'films':films})