from django.utils.text import slugify
from movies.models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie

    def create(self, validated_data):
        if not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data['title'])
        return super().create(**validated_data)
