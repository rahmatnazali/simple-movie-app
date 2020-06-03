from django.urls import path
from .views import MovieSearchView

urlpatterns = [
    path('movie/search', MovieSearchView.as_view(), name="movie-search"),
]
