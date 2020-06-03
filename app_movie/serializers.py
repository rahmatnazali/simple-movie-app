from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from app_movie.models import Movie


class MovieSearchSerializer(ModelSerializer):
    name = serializers.CharField()
    thumbnail = serializers.URLField()
    slug = serializers.SlugField()

    class Meta:
        model = Movie
        fields = ('name', 'thumbnail', 'slug')
