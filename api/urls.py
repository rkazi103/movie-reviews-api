from django.urls import path
from . import views

urlpatterns = [
    path("endpoints/", views.api_overview, name="api-overview"),
    path("movies/", views.movie_list, name="movie-list"),
    path("movie/<str:pk>", views.movie_detail, name="movie-detail"),
    path("movie-create/", views.movie_create, name="movie-create"),
    path("movie-update/<str:pk>", views.movie_update, name="movie-update"),
    path("movie-delete/<str:pk>", views.movie_delete, name="movie-delete"),
    path("movie/<str:pk>/movie-reviews/",
         views.movie_reviews_list, name="movie-reviews-list"),
    path("movie/<str:movie_pk>/movie-review/<str:movie_review_pk>",
         views.movie_reviews_detail, name="movie-reviews-detail"),
    path("movie/movie-review-create/",
         views.movie_reviews_create, name="movie-reviews-create"),
    path("movie/<str:movie_pk>/movie-review-update/<str:movie_review_pk>",
         views.movie_reviews_update, name="movie-review-update"),
    path("movie/<str:movie_pk>/movie-review-delete/<str:movie_review_pk>",
         views.movie_reviews_delete, name="movie-review-delete")
]
