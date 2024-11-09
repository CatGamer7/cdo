from rest_framework import viewsets
from games.models import Developer
from games.serializers import DeveloperSerializer


class DeveloperViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
