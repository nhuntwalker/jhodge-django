from django.db import models

# Create your models here.

class NewsItem(models.Model):
    """Links to news items."""
    title = models.CharField(max_length=1024)
    link = models.URLField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
