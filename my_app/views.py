
from django.shortcuts import render
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET', 'POST'])
def person_list(request):
    if request.method == 'GET':
        toys = Person.objects.all()
        toys_serializer = PersonSerializer(toys, many=True)
        return Response(toys_serializer.data)
    elif request.method == 'POST':
        toy_serializer = PersonSerializer(data=request.data)
        if toy_serializer.is_valid():
            toy_serializer.save()
        return Response(toy_serializer.data,
    status=status.HTTP_201_CREATED)
    return Response(toy_serializer.errors,
    status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        person_serializer = PersonSerializer(person)
        return Response(person_serializer.data)
    elif request.method == 'PUT':
        person_serializer = PersonSerializer(person_serializer, data=request.data)
        if person_serializer.is_valid():
            person_serializer.save()
            return Response(person_serializer.data)
        return Response(person_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)