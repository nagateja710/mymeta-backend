from django.contrib import admin
from .models import Media, UserMedia


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'release_year')
    list_filter = ('type',)
    search_fields = ('title',)


@admin.register(UserMedia)
class UserMediaAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'media',
        'status',
        'airing_status',
        'rating',
        'progress_watched',
        'progress_total',
    )
    list_filter = ('status', 'airing_status')
    search_fields = ('media__title', 'user__username')
