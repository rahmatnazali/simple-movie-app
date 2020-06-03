from django.urls import path
from .views import MovieList, MovieDetail

urlpatterns = [
    path('', MovieList.as_view(), name="movie-list"),
    path('<slug:slug>/', MovieDetail.as_view(), name="movie-detail"),
]
