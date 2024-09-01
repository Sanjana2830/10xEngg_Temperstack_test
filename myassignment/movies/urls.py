from django.urls import path
from .views import (
    MovieListCreateView, MovieDetailView, MovieListView,
    PerformerListCreateView, PerformerDetailView, PerformerDeleteView,
    GenreListCreateView, GenreDetailView,
    LanguageListCreateView, LanguageDetailView,
    TechnicianListCreateView, TechnicianDetailView,
    DirectorListCreateView, DirectorDetailView,
    AwardListCreateView, AwardDetailView,
    ReviewListCreateView, ReviewDetailView,
    MovieDetailListCreateView, MovieDetailDetailView
)

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/all/', MovieListView.as_view(), name='movie-list'),

    path('performers/', PerformerListCreateView.as_view(), name='performer-list-create'),
    path('performers/<int:pk>/', PerformerDetailView.as_view(), name='performer-detail'),
    path('performers/<int:pk>/delete/', PerformerDeleteView.as_view(), name='performer-delete'),

    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),

    path('languages/', LanguageListCreateView.as_view(), name='language-list-create'),
    path('languages/<int:pk>/', LanguageDetailView.as_view(), name='language-detail'),

    path('technicians/', TechnicianListCreateView.as_view(), name='technician-list-create'),
    path('technicians/<int:pk>/', TechnicianDetailView.as_view(), name='technician-detail'),

    path('directors/', DirectorListCreateView.as_view(), name='director-list-create'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),

    path('awards/', AwardListCreateView.as_view(), name='award-list-create'),
    path('awards/<int:pk>/', AwardDetailView.as_view(), name='award-detail'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    path('movie-details/', MovieDetailListCreateView.as_view(), name='movie-detail-list-create'),
    path('movie-details/<int:pk>/', MovieDetailDetailView.as_view(), name='movie-detail-detail'),
]
