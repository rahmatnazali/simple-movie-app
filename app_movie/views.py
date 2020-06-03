from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Movie

select_for_list = ('name', 'thumbnail', 'user_rating', 'genre', 'slug', 'rating', 'genre')
select_for_detail = ('name', 'thumbnail', 'description', 'language', 'duration', 'user_rating', 'genre', 'rating', 'rating_label', 'genre')


# Create your views here.
class MovieList(ListView):
    model = Movie
    queryset = Movie.objects.select_related('rating').prefetch_related('genre').order_by('-created_at').only(*select_for_list)
    paginate_by = 5
    template_name = 'movie_list.html'


class MovieDetail(DetailView):
    model = Movie
    queryset = Movie.objects.select_related('rating').prefetch_related('genre').only(*select_for_detail)
    template_name = 'movie_detail.html'
