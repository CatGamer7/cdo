from rest_framework import serializers
from games.models import Developer


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        exclude = ()
