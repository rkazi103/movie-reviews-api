from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    date_released = models.DateTimeField(
        auto_now_add=False, default=timezone.now, blank=True, null=True)
    playtime = models.IntegerField(default=60)
    trailer_link = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title
