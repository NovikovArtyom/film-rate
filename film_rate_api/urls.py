from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from film_rate_api.views import FilmViewSet, CategoriesViewSet, DirectorsViewSet, ActorsViewSet

router = SimpleRouter()
router.register('films', FilmViewSet)
router.register('categories', CategoriesViewSet)
router.register('directors', DirectorsViewSet)
router.register('actors', ActorsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]