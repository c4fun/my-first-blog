from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Movie

# Create your views here.
def movie_list(request):
    movies = Movie.objects.filter(air_time__lte=timezone.now()).order_by('air_time')
    return render(request, 'movie/movie_list.html', {'movies': movies})