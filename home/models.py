from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    LEITOR = "Leitor"
    ESCRITOR = "Escritor"
    LEITOR_OU_ESCRITOR = {
        LEITOR: "Leitor",
        ESCRITOR: "Escritor",
    }
    role = models.CharField(
        max_length=10, choices=LEITOR_OU_ESCRITOR.items(), default=LEITOR
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.username