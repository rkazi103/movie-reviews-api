from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    date_released = models.DateTimeField(
        auto_now_add=False, default=timezone.now, blank=True, null=True)
    playtime = models.IntegerField(default=60)
    trailer_link = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ("date_released",)

    def __str__(self):
        return self.title


class MovieReview(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        ordering = ("date_created",)

    def __str__(self):
        return f"Movie: {self.movie}, Review Name: {self.title}"
