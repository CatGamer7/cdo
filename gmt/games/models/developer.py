from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=64)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('name',)
