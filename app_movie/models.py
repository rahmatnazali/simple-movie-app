from django.db import models
from django.utils.text import slugify
import uuid
# Create your models here.
LANGUAGE = (
        ('EN', 'English'),
        ('KR', 'Korean'),
        ('HI', 'Hindi'),
        ('TM', 'Tamil'),
        ('MD', 'Mandarin'),
        # and so on ..
        ('-', 'N/A'),
)

class Rating(models.Model):
    name = models.CharField(max_length=10, unique=True)  # make it unique and indexed for filter/search

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=10, db_index=True)  # make it unique and indexed for filter/search

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255, db_index=True)  # indexed for filter/search
    description = models.TextField()
    thumbnail = models.URLField()
    duration = models.IntegerField()
    language = models.CharField(max_length=2, choices=LANGUAGE, db_index=True)  # could be indexed for filtering by language
    user_rating = models.FloatField()

    genre = models.ManyToManyField(Genre, related_name="movies_in_genre")
    rating = models.ForeignKey(Rating, on_delete=models.DO_NOTHING, related_name="movies_in_rating", null=True, blank=True)
    rating_label = models.CharField(max_length=100)  # I put the rating label here, because movies withthe same MPAA Rating could have different label

    slug = models.SlugField(unique=True) # make it unique and indexed for url hit
    created_at = models.DateTimeField(auto_now_add=True, db_index=True) # make it indexed for sorting

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.id is None or (self.slug is not None and slugify(self.name) not in self.slug):
            self.slug = slugify(f"{self.name}-{str(uuid.uuid4())[:8]}")
        super().save(force_insert, force_update, using, update_fields)

