from django.contrib import admin
from .models import Movie, Rating, Genre

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    filter_horizontal = ('genre',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Genre, GenreAdmin)