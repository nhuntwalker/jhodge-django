from django.contrib import admin
from awards.models import Award

# Register your models here.
@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    """Dictating how Awards will appear in the Django admin."""
    list_display = [
        'festival', 'year', 'film'
    ]
    ordering = ('date_posted',)