from django.db import models

from apps.authentication.infrastructure.models import CustomUser


class Device(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.ip})"