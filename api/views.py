"""DISCLAMIMER: Movie API Views are most abstract because they are the most generalized and easiest to write"""

from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, MovieReview
from .serializers import MovieSerializer, MovieReviewSerializer
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404


def overview(request):
    return redirect("/api/")


class APIOverview(APIView):
    """Give an Overview of the API"""

    def get(self, request, format=None) -> Response:
        response = {
            "Go to the following link to see the API Reference": "https://github.com/rkazi103/movie-reviews-api/blob/main/API_REFERENCE.md"
        }

        return Response(response)


class MovieListView(generics.ListCreateAPIView):
    """Get all movies or create new one"""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Get, update, or delete a specific movie"""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieReviewListView(APIView):
    """Get movie reviews or create a new movie review for a specific movie"""

    def get(self, request, pk, format=None) -> Response:
        try:
            movie = Movie.objects.get(id=pk)
            movie_reviews = MovieReview.objects.filter(movie=movie.id)
        except Movie.DoesNotExist or MovieReview.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieReviewSerializer(movie_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None, format=None) -> Response:
        serializer = MovieReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieReviewDetailsView(APIView):
    """Get, update, or delete a specific movie review for a specific movie"""

    def get_object(self, movie_pk, movie_review_pk):
        if movie_pk == None or movie_review_pk == None:
            raise ValueError

        try:
            movie = Movie.objects.get(pk=movie_pk)
            movie_reviews = MovieReview.objects.filter(movie=movie.id)
            movie_review = movie_reviews.get(id=movie_review_pk)
            return movie_review
        except Movie.DoesNotExist or MovieReview.DoesNotExist:
            raise Http404

    def get(self, request, movie_pk, movie_review_pk) -> Response:
        movie_review = self.get_object(movie_pk, movie_review_pk)
        print(movie_review)
        serializer = MovieReviewSerializer(movie_review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, movie_pk, movie_review_pk) -> Response:
        movie_review = self.get_object(movie_pk, movie_review_pk)
        serializer = MovieReviewSerializer(
            instance=movie_review, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, movie_pk, movie_review_pk):
        movie_review = self.get_object(movie_pk, movie_review_pk)
        movie_review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
