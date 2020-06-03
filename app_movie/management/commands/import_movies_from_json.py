from django.core.management.base import BaseCommand
from oas_movie_app.settings import BASE_DIR
from app_movie.models import Movie, Genre, Rating, LANGUAGE
from pathlib import Path
import json

def map_language(language):
    for key, value in LANGUAGE:
        if language == value:
            return key
    return "-"

class Command(BaseCommand):
    help = 'Import movie data from json'

    def handle(self, *args, **options):
        root_path = Path(BASE_DIR)
        with (root_path / "movies.json").open() as i:
            movie_list = json.load(i)

            for movie in movie_list:
                # for simplicity I assume that all movies data in json didn't contain missing values

                # todo: upload thumbnail to s3

                # get or create mpaa_rating
                mpaa_rating = movie.get("mpaaRating")
                mpaa_rating_type = mpaa_rating.get("type")
                rating, rating_created = Rating.objects.get_or_create(name=mpaa_rating_type, defaults={'name': mpaa_rating_type})
                if rating_created: print(f"created Rating {rating.name}")

                m = Movie.objects.create(
                    name=movie.get("name"),
                    description=movie.get("description"),
                    duration=int(movie.get("duration", 0)),
                    language=map_language(movie.get("language")),
                    user_rating=int(movie.get("userRating", 0)),
                    rating=rating,
                    rating_label=mpaa_rating.get("label"),
                )

                # get or create genre
                genres = movie.get("genre")
                genre_ids = []
                for genre in genres:
                    g, created = Genre.objects.get_or_create(name=genre, defaults={'name': genre})
                    if created: print(f"created Genre {g.name}")
                    genre_ids.append(g.id)
                m.genre.add(*genre_ids)
