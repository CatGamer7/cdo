from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ('name',)
