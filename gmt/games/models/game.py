from django.db import models
from .developer import Developer
from .genre import Genre


class Game(models.Model):
    name = models.CharField(max_length=64)
    date_published = models.DateTimeField(auto_now_add=True)
    developer = models.ForeignKey(
        Developer,
        on_delete=models.CASCADE,
        related_name="games"
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name="games"
    )

    class Meta:
        ordering = ('name',)
