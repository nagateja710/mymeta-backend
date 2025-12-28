from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from media.views import UserMediaViewSet, add_to_library
from users.views import signup  # ✅ single signup source

# 🔥 Router for UserMedia
router = DefaultRouter()
router.register(r"user-media", UserMediaViewSet, basename="user-media")

urlpatterns = [
    path("", lambda r: JsonResponse({"status": "MyMeta API running"})),

    path("admin/", admin.site.urls),

    # 🔐 AUTH
    path("api/auth/login/", TokenObtainPairView.as_view()),
    path("api/auth/signup/", signup),
    path("api/auth/refresh/", TokenRefreshView.as_view()),

    # 📚 ADD MEDIA
    path("api/add-to-library/", add_to_library),

    # 🔥 USER MEDIA CRUD
    path("api/", include(router.urls)),
]
