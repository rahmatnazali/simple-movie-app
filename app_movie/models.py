from django.db import models

# Create your models here.

class Rating(models.Model):
    name = models.CharField(max_length=10, unique=True)  # make it unique and indexed for filter/search

class Genre(models.Model):
    name = models.CharField(max_length=10, db_index=True)  # make it unique and indexed for filter/search

class Movie(models.Model):
    name = models.CharField(max_length=255, db_index=True)  # indexed for filter/search
    description = models.TextField()
    thumbnail = models.URLField()
    duration = models.IntegerField()
    language = models.CharField(max_length=2, choices=(
        ('EN', 'English'),
        ('KR', 'Korean'),
        ('HI', 'Hindi'),
        ('TM', 'Tamil'),
        ('MD', 'Mandarin'),
        # and so on ..
    ))
    user_rating = models.FloatField()

    genre = models.ManyToManyField(Genre, related_name="movies_in_genre")
    rating = models.ForeignKey(Rating, on_delete=models.DO_NOTHING, related_name="movies_in_rating")
    rating_label = models.CharField(max_length=100)  # I put the rating label here, because movies withthe same MPAA Rating could have different label
