from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, MovieReview
from .serializers import MovieSerializer, MovieReviewSerializer


def overview(request):
    return redirect("/api/endpoints")


@api_view(["GET"])
def api_overview(request):
    response = {
        "Go to the following link to see the API Reference": "https://github.com/rkazi103/movie-reviews-api/blob/main/API_REFERENCE.md"
    }

    return Response(response)


@api_view(["GET"])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def movie_create(request):
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def movie_update(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MovieSerializer(instance=movie, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def movie_delete(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def movie_reviews_list(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
        movie_reviews = MovieReview.objects.filter(movie=movie.id)
    except Movie.DoesNotExist or MovieReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MovieReviewSerializer(movie_reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def movie_reviews_detail(request, movie_pk, movie_review_pk):
    try:
        movie = Movie.objects.get(id=movie_pk)
        movie_reviews = MovieReview.objects.filter(movie=movie.id)
        movie_review = movie_reviews.get(id=movie_review_pk)
    except Movie.DoesNotExist or MovieReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    print(movie, movie_review)

    serializer = MovieReviewSerializer(movie_review)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def movie_reviews_create(request):
    serializer = MovieReviewSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def movie_reviews_update(request, movie_pk, movie_review_pk):
    try:
        movie = Movie.objects.get(id=movie_pk)
        movie_reviews = MovieReview.objects.filter(movie=movie.id)
        movie_review = movie_reviews.get(id=movie_review_pk)
    except Movie.DoesNotExist or MovieReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MovieReviewSerializer(
        instance=movie_review, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def movie_reviews_delete(request, movie_pk, movie_review_pk):
    try:
        movie = Movie.objects.get(pk=movie_pk)
        movie_reviews = MovieReview.objects.filter(movie=movie.id)
        movie_review = movie_reviews.get(id=movie_review_pk)
    except Movie.DoesNotExist or MovieReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    movie_review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
