from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    prize = models.CharField(max_length=64, null=True)
    year = models.PositiveSmallIntegerField(default=2000)
    review = models.TextField(default='')
    premiere = models.DateField(null=True, blank=True)
    imbd_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)

    def title_with_year(self):
        return '{} ({})'.format(str(self.title), str(self.year))

    def __str__(self):
        return self.title_with_year()





