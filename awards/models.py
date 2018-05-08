from django.db import models
from films.models import Film
import datetime


YEAR_CHOICES = []
for yr in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((yr, yr))


class Award(models.Model):
    """Awards for films."""
    festival = models.CharField(max_length=1024)
    year = models.IntegerField(choices=YEAR_CHOICES[::-1])
    designation = models.CharField(max_length=1024)
    laurel = models.ImageField(upload_to="laurels")
    date_posted = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.festival} - {self.year}"
