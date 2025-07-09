from rest_framework import viewsets

from film_rate_api.models import Film, Category, Director, Actor
from film_rate_api.serializers import FilmSerializer, CategoriesSerializer, DirectorsSerializer, ActorsSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class DirectorsViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorsSerializer


class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorsSerializer