from django.shortcuts import render
from rest_framework import viewsets, permissions
from movies.serializers import MovieSerializer
from movies.models import Movie

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
