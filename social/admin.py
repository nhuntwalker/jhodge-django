from django.contrib import admin
from social.models import SocialLink

# Register your models here.
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    """Dictating how social links will appear in the Django admin."""
    fields = ['social_media_type', 'link', 'order', 'icon_class']
    list_display = ['social_media_type', 'link', 'order']
    ordering = ('order',)