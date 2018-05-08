from django.db import models

# Create your models here.

class Film(models.Model):
    """The films."""
    title = models.CharField(max_length=1024)
    release_date = models.DateField()
    genres = models.TextField()
    credits = models.CharField(max_length=1024)
    trailer = models.URLField(blank=True, null=True)
    description = models.TextField()
    excerpt = models.TextField(max_length=85)
    slug = models.SlugField()
    slider_text = models.TextField()
    film_types = models.CharField(max_length=100, verbose_name="Film Type(s)")
    screenshot = models.ImageField(upload_to='screenshots')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.release_date.strftime('%Y')}"
