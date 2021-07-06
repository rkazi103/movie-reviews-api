from django.urls import path
from . import views
from .views import MovieListView, MovieDetailsView, APIOverview, MovieReviewListView, MovieReviewDetailsView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("", APIOverview.as_view(), name="api-overview"),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movie/<str:pk>/", MovieDetailsView.as_view(), name="movie-crud"),
    path("movie/<str:pk>/movie-reviews/",
         MovieReviewListView.as_view(), name="movie-review-list"),
    path("movie/<str:movie_pk>/movie-review/<str:movie_review_pk>/",
         MovieReviewDetailsView.as_view(), name="movie-reviews-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
