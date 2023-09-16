from rest_framework import serializers
from movies.models import Movie, Choices, MovieOrder
from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(choices=Choices.choices, default=Choices.G)
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.EmailField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source="movie.title", read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
