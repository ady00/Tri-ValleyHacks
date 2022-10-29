from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Painting

class PaintingView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Painting.objects.all()



