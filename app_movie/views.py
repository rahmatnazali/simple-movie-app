from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Movie
from rest_framework import generics
from rest_framework import filters
from rest_framework import pagination
from rest_framework import response
from .serializers import MovieSearchSerializer

select_for_list = ('name', 'thumbnail', 'user_rating', 'duration', 'slug', 'rating')
select_for_detail = ('name', 'thumbnail', 'description', 'language', 'duration', 'user_rating', 'genre', 'rating', 'rating_label', 'genre')


# Create your views here.
class MovieList(ListView):
    model = Movie
    queryset = Movie.objects.select_related('rating').order_by('-created_at').only(*select_for_list)
    paginate_by = 5
    template_name = 'movie_list.html'


class MovieDetail(DetailView):
    model = Movie
    queryset = Movie.objects.select_related('rating').prefetch_related('genre').only(*select_for_detail)
    template_name = 'movie_detail.html'


class MovieSearchPagination(pagination.LimitOffsetPagination):
    default_limit = 5


class MovieSearchView(generics.ListAPIView):
    queryset = Movie.objects.only('name')
    serializer_class = MovieSearchSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = MovieSearchPagination

    def get_paginated_response(self, data):
        return response.Response(data)
