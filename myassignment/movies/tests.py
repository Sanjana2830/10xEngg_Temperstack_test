from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Movie, Performer, Genre, Language, Technician, Director

class MovieModelTests(TestCase):

    def setUp(self):
        # Create some test data
        self.genre = Genre.objects.create(name="Action")
        self.language = Language.objects.create(name="English", code="en")
        self.technician = Technician.objects.create(
            name="Christopher Nolan", role="Director", date_of_birth="1970-07-30"
        )
        self.director = Director.objects.create(technician=self.technician)
        self.performer = Performer.objects.create(
            name="Leonardo DiCaprio", gender="M", date_of_birth="1974-11-11"
        )
        self.movie = Movie.objects.create(
            name="Inception",
            year_of_release=2010,
            rating=8.8,
            description="A thief who steals corporate secrets through the use of dream-sharing technology.",
            duration=148,
            director=self.director,
        )
        self.movie.genres.add(self.genre)
        self.movie.languages.add(self.language)
        self.movie.performers.add(self.performer)

    def test_movie_creation(self):
        """Test if the movie is created with correct details"""
        movie = Movie.objects.get(name="Inception")
        self.assertEqual(movie.year_of_release, 2010)
        self.assertEqual(movie.rating, 8.8)
        self.assertEqual(movie.description[:6], "A thie")
        self.assertEqual(movie.director.technician.name, "Christopher Nolan")
        self.assertIn(self.genre, movie.genres.all())
        self.assertIn(self.language, movie.languages.all())
        self.assertIn(self.performer, movie.performers.all())

    def test_string_representation(self):
        """Test the string representation of the Movie model"""
        movie = Movie.objects.get(name="Inception")
        self.assertEqual(str(movie), movie.name)

class MovieViewTests(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.genre = Genre.objects.create(name="Action")
        self.language = Language.objects.create(name="English", code="en")
        self.technician = Technician.objects.create(
            name="Christopher Nolan", role="Director", date_of_birth="1970-07-30"
        )
        self.director = Director.objects.create(technician=self.technician)
        self.performer = Performer.objects.create(
            name="Leonardo DiCaprio", gender="M", date_of_birth="1974-11-11"
        )
        self.movie = Movie.objects.create(
            name="Inception",
            year_of_release=2010,
            rating=8.8,
            description="A thief who steals corporate secrets through the use of dream-sharing technology.",
            duration=148,
            director=self.director,
        )
        self.movie.genres.add(self.genre)
        self.movie.languages.add(self.language)
        self.movie.performers.add(self.performer)

    def test_get_all_movies(self):
        """Test getting all movies"""
        url = reverse('movie-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return 1 movie

    def test_get_single_movie(self):
        """Test getting a single movie"""
        url = reverse('movie-detail', kwargs={'pk': self.movie.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Inception')

    def test_create_movie(self):
        """Test creating a new movie"""
        url = reverse('movie-list-create')
        data = {
            "name": "The Dark Knight",
            "year_of_release": 2008,
            "rating": 9.0,
            "description": "When the menace known as The Joker emerges, he creates chaos.",
            "duration": 152,
            "director": self.director.id,
            "genres": [self.genre.id],
            "languages": [self.language.id],
            "performers": [self.performer.id],
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)

    def test_update_movie(self):
        """Test updating an existing movie"""
        url = reverse('movie-detail', kwargs={'pk': self.movie.id})
        data = {
            "name": "Inception Updated",
            "year_of_release": 2010,
            "rating": 8.9,
            "description": "Updated description",
            "duration": 150,
            "director": self.director.id,
            "genres": [self.genre.id],
            "languages": [self.language.id],
            "performers": [self.performer.id],
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.name, "Inception Updated")

    def test_delete_movie(self):
        """Test deleting a movie"""
        url = reverse('movie-detail', kwargs={'pk': self.movie.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)
