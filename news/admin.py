from django.contrib import admin
from news.models import NewsItem

# Register your models here.
@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    """Dictating how news items will appear in the Django admin."""
    list_display = ['title', 'link', 'date_posted']
    ordering = ('-date_posted',)