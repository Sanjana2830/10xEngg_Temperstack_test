from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import filters
from .models import Movie, Performer, Genre, Language, Technician, Director, Award, Review, MovieDetail
from .serializers import MovieSerializer, PerformerSerializer, GenreSerializer, LanguageSerializer, TechnicianSerializer, DirectorSerializer, AwardSerializer, ReviewSerializer, MovieDetailSerializer



# Home view
def home(request):
    return HttpResponse("<h1>Welcome to the Movie Database API</h1><p>Use /api/ to access the endpoints.</p>")

def api_index(request):
    endpoints = {
        "movies": "/api/movies/",
        "performers": "/api/performers/",
        "genres": "/api/genres/",
        "languages": "/api/languages/",
        "technicians": "/api/technicians/",
        "directors": "/api/directors/",
        "awards": "/api/awards/",
        "reviews": "/api/reviews/",
        "movie-details": "/api/movie-details/",
    }
    return JsonResponse({"available_endpoints": endpoints})



# GET/POST for Movies: Fetching, Adding, and Updating movies
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['year_of_release', 'rating']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# GET for a Single Movie (Retrieve, Update, Delete)
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# GET All Movies: Pagination, Filtering, and Searching
class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['year_of_release', 'rating']

    def get_queryset(self):
        queryset = Movie.objects.all()
        genre = self.request.query_params.get('genre', None)
        if genre is not None:
            queryset = queryset.filter(genres__name__icontains=genre)
        return queryset

# GET/POST for Performers: Fetching, Adding, and Updating performers
class PerformerListCreateView(generics.ListCreateAPIView):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'biography']
    ordering_fields = ['date_of_birth']

# GET for a Single Performer (Retrieve, Update, Delete)
class PerformerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer

# DELETE a Performer (Actor/Actress): Safely delete an actor
class PerformerDeleteView(generics.DestroyAPIView):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.movie_set.exists():  # Ensure the performer is not associated with any movies
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"detail": "Cannot delete performer as they are associated with one or more movies."},
                status=status.HTTP_400_BAD_REQUEST
            )

# GET/POST for Genres: Fetching, Adding, and Updating genres
class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# GET for a Single Genre (Retrieve, Update, Delete)
class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# GET/POST for Languages: Fetching, Adding, and Updating languages
class LanguageListCreateView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

# GET for a Single Language (Retrieve, Update, Delete)
class LanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

# GET/POST for Technicians: Fetching, Adding, and Updating technicians
class TechnicianListCreateView(generics.ListCreateAPIView):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'biography']
    ordering_fields = ['date_of_birth']

# GET for a Single Technician (Retrieve, Update, Delete)
class TechnicianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer

# GET/POST for Directors: Fetching, Adding, and Updating directors
class DirectorListCreateView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

# GET for a Single Director (Retrieve, Update, Delete)
class DirectorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

# GET/POST for Awards: Fetching, Adding, and Updating awards
class AwardListCreateView(generics.ListCreateAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

# GET for a Single Award (Retrieve, Update, Delete)
class AwardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

# GET/POST for Reviews: Fetching, Adding, and Updating reviews
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# GET for a Single Review (Retrieve, Update, Delete)
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# GET/POST for Movie Details: Fetching, Adding, and Updating movie details
class MovieDetailListCreateView(generics.ListCreateAPIView):
    queryset = MovieDetail.objects.all()
    serializer_class = MovieDetailSerializer

# GET for a Single Movie Detail (Retrieve, Update, Delete)
class MovieDetailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieDetail.objects.all()
    serializer_class = MovieDetailSerializer
