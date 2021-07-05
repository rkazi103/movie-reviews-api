from .models import Movie, MovieReview
from rest_framework import serializers


class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = ["title", "content",  "date_created", "movie"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
