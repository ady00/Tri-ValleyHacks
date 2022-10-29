from rest_framework import serializers
from .models import Painting

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ('id', 'title', 'time_period', 'location', 'artist')