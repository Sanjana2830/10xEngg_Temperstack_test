from django.db import models

# Language Model (Many-to-Many with Movie)
class Language(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    code = models.CharField(max_length=10, unique=True, null=False)

    def __str__(self):
        return self.name
    
# Genre Model
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name

# Performer Model with Gender Field (Many-to-Many with Movie)
class Performer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),  # Optional: For non-binary or other genders
    ]
    name = models.CharField(max_length=255, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.name

# Technician Model (One-to-One with Director, Many-to-Many with Movie)
class Technician(models.Model):
    ROLE_CHOICES = [
        ('Director', 'Director'),
        ('Producer', 'Producer'),
        ('Cinematographer', 'Cinematographer'),
        # Add other roles as needed
    ]
    name = models.CharField(max_length=255, null=False)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, null=False)
    date_of_birth = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.role})"

# Director Model (One-to-One with Technician, Many-to-One with Movie)
class Director(models.Model):
    technician = models.OneToOneField(Technician, on_delete=models.CASCADE, related_name='directed_movies')
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.technician.name

# Award Model (Many-to-Many with Movie through MovieAward)
class Award(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    category = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.name} - {self.category}"

# Movie Model (Central Model)
class Movie(models.Model):
    name = models.CharField(max_length=255, null=False)
    year_of_release = models.IntegerField(null=False)
    rating = models.FloatField(null=False)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name='movies')
    genres = models.ManyToManyField(Genre, through='MovieGenre')
    performers = models.ManyToManyField(Performer, through='MoviePerformer')
    technicians = models.ManyToManyField(Technician, through='MovieTechnician')
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
    
# MoviePerformer Join Table (Many-to-Many Relationship with Extra Data)
class MoviePerformer(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('movie', 'performer')

    def __str__(self):
        return f"{self.movie.name} - {self.performer.name}"

# MovieTechnician Join Table (Many-to-Many Relationship with Extra Data)
class MovieTechnician(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('movie', 'technician')

    def __str__(self):
        return f"{self.movie.name} - {self.technician.name}"

# MovieGenre Join Table (Many-to-Many Relationship with Extra Data)
class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('movie', 'genre')

    def __str__(self):
        return f"{self.movie.name} - {self.genre.name}"
    
# MovieAward Join Table (Many-to-Many Relationship with Extra Data)
class MovieAward(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    year = models.IntegerField(null=False)

    class Meta:
        unique_together = ('movie', 'award', 'year')

    def __str__(self):
        return f"{self.movie.name} won {self.award.name} in {self.year}"
    
# Review Model (One-to-Many Relationship)
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=255, null=False)
    review_text = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=False)

    def __str__(self):
        return f"Review by {self.reviewer_name} for {self.movie.name}"

# MovieDetail Model (One-to-One Relationship)
class MovieDetail(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, related_name='details')
    synopsis = models.TextField(null=True, blank=True)
    trivia = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Details for {self.movie.name}"