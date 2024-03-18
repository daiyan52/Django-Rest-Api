from django.shortcuts import render
from testapp.models import Actor, Movie
from testapp.Serializers import ActorSerializer,MovieSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

class ActorListView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
class ActorView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class MovieView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer