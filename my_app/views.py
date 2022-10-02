from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import Person
# Create your views here


class PersonView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
