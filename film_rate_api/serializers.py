from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils import timezone

from film_rate_api.models import Film, Category, Director, Actor, BaseModel

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'email', 'username', 'first_name', 'last_name']


class BaseModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    updated_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = BaseModel
        fields = ['id', 'created_at', 'created_by', 'updated_at', 'updated_by']

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['created_by'] = user.pk
            validated_data['created_at'] = timezone.now()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['updated_by'] = user.pk
            validated_data['updated_at'] = timezone.now()

        return super().update(instance, validated_data)


class CategoriesSerializer(BaseModelSerializer):
    class Meta:
        model = Category
        fields = BaseModelSerializer.Meta.fields + ['title', 'description']


class DirectorsSerializer(BaseModelSerializer):
    class Meta:
        model = Director
        fields = BaseModelSerializer.Meta.fields + ['first_name', 'last_name', 'birth_date', 'country']


class ActorsSerializer(BaseModelSerializer):
    class Meta:
        model = Actor
        fields = BaseModelSerializer.Meta.fields + ['first_name', 'last_name', 'birth_date', 'country']


class FilmListSerializer(BaseModelSerializer):
    class Meta:
        model = Film
        fields = BaseModelSerializer.Meta.fields + ['title', 'description', 'release_year', 'duration', 'rating', 'category', 'director', 'actor']


class FilmSerializer(BaseModelSerializer):
    category = CategoriesSerializer(read_only=True, many=True)
    director = DirectorsSerializer(read_only=True)
    actor = ActorsSerializer(read_only=True, many=True)

    class Meta:
        model = Film
        fields = BaseModelSerializer.Meta.fields + ['title', 'description', 'release_year', 'duration', 'rating', 'category', 'director', 'actor']