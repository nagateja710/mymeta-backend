from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django.utils import timezone

from .models import Media, UserMedia
from .serializers import UserMediaSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_library(request):
    data = request.data
    user = request.user

    # 1️⃣ Create or reuse Media (GLOBAL DATA ONLY)
    media, _ = Media.objects.get_or_create(
        title=data["title"],
        type=data["type"],
        defaults={
            "release_year": data.get("release_year"),
            "cover_url": data.get("cover_url", ""),
        }
    )

    # 2️⃣ Defaults for UserMedia
    defaults = {
        "status": "todo",
        "airing_status": "unknown",
        "rating": 0,
        "progress_watched": 0,
        "progress_total": 0,
        "synopsis": data.get("synopsis", ""),
        "notes": data.get("notes", ""),
        "updated_at": timezone.now(),
    }

    # 3️⃣ Allow overrides (Advanced Add)
    for field in [
        "status",
        "airing_status",
        "rating",
        "progress_watched",
        "progress_total",
        "synopsis",
        "notes",
    ]:
        if field in data:
            defaults[field] = data[field]

    # 4️⃣ Create UserMedia
    user_media, created = UserMedia.objects.get_or_create(
        user=user,  
        media=media,
        defaults=defaults,
    )

    if not created:
        return Response(
            {"detail": "Already in library"},
            status=status.HTTP_200_OK,
        )

    return Response(
        UserMediaSerializer(user_media).data,
        status=status.HTTP_201_CREATED,
    )


class UserMediaViewSet(ModelViewSet):
    serializer_class = UserMediaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserMedia.objects.filter(user=self.request.user)

    # def perform_update(self, serializer):
    #     serializer.save(updated_at=timezone.now())
