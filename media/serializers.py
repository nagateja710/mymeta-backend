from rest_framework import serializers
from .models import Media, UserMedia


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = [
            "id",
            "title",
            "type",
            "release_year",
            "cover_url",
        ]


class UserMediaSerializer(serializers.ModelSerializer):
    media = MediaSerializer()  # 🔥 THIS IS THE FIX

    class Meta:
        model = UserMedia
        fields = [
            "id",

            "status",
            "airing_status",
            "rating",
            "progress_watched",
            "progress_total",
            "updated_at",
            "synopsis",
            "notes",
            "media",
        ]
