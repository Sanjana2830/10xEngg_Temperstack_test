from rest_framework import serializers
from .models import Language, Genre, Performer, Technician, Director, Award, Movie, MoviePerformer, MovieTechnician, MovieGenre, MovieAward, Review, MovieDetail

# Language Serializer
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

# Genre Serializer
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# Performer Serializer
class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = '__all__'

# Technician Serializer
class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = '__all__'

# Director Serializer
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

# Award Serializer
class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'

# Movie Serializer
class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    performers = PerformerSerializer(many=True, read_only=True)
    technicians = TechnicianSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

# MoviePerformer Serializer (Join Table)
class MoviePerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePerformer
        fields = '__all__'

# MovieTechnician Serializer (Join Table)
class MovieTechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieTechnician
        fields = '__all__'

# MovieGenre Serializer (Join Table)
class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = '__all__'

# MovieAward Serializer (Join Table)
class MovieAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieAward
        fields = '__all__'

# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# MovieDetail Serializer
class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDetail
        fields = '__all__'
