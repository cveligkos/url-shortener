from django.db import models
from django.core.validators import URLValidator, RegexValidator


class Link(models.Model):
    url = models.CharField(
        max_length=1000,
        unique=True,
        null=False,
        validators=[URLValidator(schemes=["https"])],
    )
    hash = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        validators=[RegexValidator(regex="[A-Za-z0-9]{5}")],
    )
    visits = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.url
