from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)

    is_reader = models.BooleanField(default=False)
    is_journalist = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if self.is_admin:
            self.is_staff = True
            self.is_superuser = True
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.username} ({'Admin' if self.is_admin else 'Jornalista' if self.is_journalist else 'Leitor'})"
