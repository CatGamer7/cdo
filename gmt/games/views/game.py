from rest_framework import viewsets
from games.models import Game
from games.serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
