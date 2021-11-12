from django.db import models


class ExtraInfo(models.Model):
    genre_dict = {(0, 'Other'),
                  (1, 'Action film'),
                  (2, 'Adventure film'),
                  (3, 'Animated film'),
                  (4, 'Comedy film'),
                  (5, 'Drama'),
                  (6, 'Fantasy film'),
                  (7, 'Historical film'),
                  (8, 'Horror film'),
                  (9, 'Science fiction film'),
                  (10, 'Thriller film'),
                  (11, 'Western')}

    duration = models.PositiveSmallIntegerField(default=0)
    film_genre = models.PositiveSmallIntegerField(default=0, choices=genre_dict)


# Main Class + One to one class
class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    prize = models.CharField(max_length=64, null=True)
    year = models.PositiveSmallIntegerField(default=2000)
    review = models.TextField(default='')
    premiere = models.DateField(null=True, blank=True)
    imbd_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)
    extra = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE, null=True, blank=True)

    def title_with_year(self):
        return '{} ({})'.format(str(self.title), str(self.year))

    def __str__(self):
        return self.title_with_year()


# One to Many
class Opinion(models.Model):
    personal_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    personal_review = models.TextField(default='')
    film_title = models.ForeignKey(Film, on_delete=models.CASCADE)


# Many to many
class Actor(models.Model):
    name = models.CharField(max_length=32, blank=False, unique=True)
    surname = models.CharField(max_length=32, blank=False, unique=True)
    film_perforn = models.ManyToManyField(Film)

