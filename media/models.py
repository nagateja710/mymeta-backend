from django.db import models
from django.contrib.auth.models import User


class Media(models.Model):
    MEDIA_TYPES = [
        ('book', 'Book'),
        ('movie', 'Movie'),
        ('anime', 'Anime'),
        ('game', 'Game'),
    ]

    type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    title = models.CharField(max_length=255)

    cover_url = models.URLField(blank=True)
    release_year = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.type})"


class UserMedia(models.Model):
    USER_STATUS = [
        ('todo', 'Todo'),
        ('doing', 'Doing'),
        ('completed', 'Completed'),
    ]

    AIRING_STATUS = [
        ('airing', 'Airing'),
        ('completed', 'Completed'),
        ('hiatus', 'Hiatus'),
        ('unknown', 'Unknown'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=15,
        choices=USER_STATUS,
        default='todo'
    )

    airing_status = models.CharField(
        max_length=20,
        choices=AIRING_STATUS,
        default='unknown'
    )

    rating = models.FloatField(default=0)

    progress_watched = models.IntegerField(default=0)
    progress_total = models.IntegerField(default=0)

    # 👇 MOVED FROM Media
    synopsis = models.TextField(blank=True)

    # 👇 NEW FIELD
    notes = models.TextField(blank=True)

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)


    class Meta:
        unique_together = ('user', 'media')

    def __str__(self):
        return f"{self.user.username} → {self.media.title}"
