from django.contrib.auth import get_user_model
from rest_framework import serializers

from film_rate_api.models import Film, Category, Director, Actor

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'email', 'login', 'first_name', 'last_name']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']


class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name', 'birth_date', 'country', 'created_at', 'updated_at']


class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'birth_date', 'country', 'created_at', 'updated_at']


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'description', 'release_year', 'duration', 'rating', 'created_at', 'updated_at']