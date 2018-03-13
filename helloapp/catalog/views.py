from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ArtistsSerializer
from .models import Artists

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new artists."""
        serializer.save()