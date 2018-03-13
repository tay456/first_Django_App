from rest_framework import serializers
from .models import Artists

class ArtistsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Artists
        fields = ('id', 'brand_name', 'manager', 'contact_number', 'contact_email', 'country')
