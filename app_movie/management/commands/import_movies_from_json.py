from django.core.management.base import BaseCommand
from oas_movie_app.settings import BASE_DIR
import json
from pathlib import Path

class Command(BaseCommand):
    help = 'Import movie data from json'

    def handle(self, *args, **options):
        root_path = Path(BASE_DIR)
        with (root_path / "movies.json").open() as i:
            movie_list = json.load(i)
            for movie in movie_list:
                print(movie.get("id"))
                print(movie.get("name"))
