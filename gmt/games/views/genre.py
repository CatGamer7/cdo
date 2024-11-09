from rest_framework import viewsets
from games.models import Genre
from games.serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
