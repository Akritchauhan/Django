from django.contrib import admin, messages
from django.core.cache import cache
from .models import YoutubeUser

@admin.action(description='Clear users cache')
def clear_users_cache(modeladmin, request, queryset):
    cache.delete('users_data')
    messages.success(request, "Users cache cleared successfully!")

@admin.register(YoutubeUser)
class YouTubeUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribers')
    actions = [clear_users_cache]