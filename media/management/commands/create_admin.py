from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = "Create or reset admin user"

    def handle(self, *args, **kwargs):
        username = os.environ.get("ADMIN_USERNAME", "naga")
        password = os.environ.get("ADMIN_PASSWORD", "admin123")

        user, created = User.objects.get_or_create(username=username)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS("Admin user created"))
        else:
            self.stdout.write(self.style.SUCCESS("Admin password reset"))
