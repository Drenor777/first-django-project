from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    prize = models.CharField(max_length=64, null=True)
    year = models.PositiveSmallIntegerField(default=2000)

    def __str__(self):
        return str(self.title) + '(' + str(self.year) + ')'
