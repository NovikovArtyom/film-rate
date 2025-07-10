from rest_framework import viewsets

from film_rate_api.models import Film, Category, Director, Actor
from film_rate_api.serializers import FilmListSerializer, CategoriesSerializer, DirectorsSerializer, ActorsSerializer, \
    FilmSerializer


class BaseViewSet(viewsets.ModelViewSet):
    def finalize_response(self, request, response, *args, **kwargs):
        if not hasattr(response, 'message'):
            response.message = None
        return super().finalize_response(request, response, *args, **kwargs)


class FilmViewSet(BaseViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            return FilmListSerializer
        return FilmSerializer


class CategoriesViewSet(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class DirectorsViewSet(BaseViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorsSerializer


class ActorsViewSet(BaseViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorsSerializer