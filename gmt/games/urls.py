from django.urls import path, include
from rest_framework.routers import DefaultRouter
from games.views import GameViewSet, GenreViewSet, DeveloperViewSet


router = DefaultRouter()
router.register(r'game', GameViewSet, basename='game')
router.register(r'genre', GenreViewSet, basename='genre')
router.register(r'developer', DeveloperViewSet, basename='developer')

urlpatterns = [
    path('', include(router.urls))
]