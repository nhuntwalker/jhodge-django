from django.db import models

# Create your models here.

class SocialLink(models.Model):
    """A simple link to a social media page."""
    link = models.URLField()
    icon_class = models.CharField(max_length=100)
    social_media_type = models.CharField(max_length=100)
    order = models.IntegerField(verbose_name="Menu Order")

    def __str__(self):
        return self.social_media_type
