from rest_framework import serializers
from games.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ()
