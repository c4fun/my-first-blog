from django.db import models
from django.utils import timezone

class Movie(models.Model):
    MOVIE_WITHES = (
        ('WH', 'wife, husband, bf, gf'),
        ('CH', 'children'),
        ('PA', 'parents'),
        ('EV', 'everyone'),
        ('BRO', 'brothers'),
        ('SIS', 'sisters'),
        ('LO', 'lover'),
    )
    name = models.CharField(max_length=200)
    air_time = models.DateTimeField(default=timezone.now)
    rank = models.IntegerField()
    score = models.FloatField()
    movie_with = models.CharField(max_length=3, choices=MOVIE_WITHES)
    critics = models.TextField(default="No Critics.")
    picture_url = models.URLField(max_length=255, default="")

    def __str__(self):
        return self.name