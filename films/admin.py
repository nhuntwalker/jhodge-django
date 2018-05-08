from django.contrib import admin
from films.models import Film

# Register your models here.
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    """Dictating how films will appear in the Django admin."""
    list_display = [
        'title', 'release_date', 'date_posted'
    ]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('date_posted',)