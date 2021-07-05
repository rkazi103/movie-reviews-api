from django.urls import path
from . import views

urlpatterns = [
    path("endpoints/", views.api_overview, name="api-overview"),
    path("movies/", views.movie_list, name="movie-list"),
    path("movie/<str:pk>", views.movie_detail, name="movie-detail"),
    path("movie-create/", views.movie_create, name="movie-create"),
    path("movie-update/<str:pk>", views.movie_update, name="movie-update"),
    path("movie-delete/<str:pk>", views.movie_delete, name="movie-delete"),
]
