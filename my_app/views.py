
from django.shortcuts import render
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def notes_list(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        notes_serializer = NoteSerializer(notes, many=True)
        return Response(notes_serializer.data)
    elif request.method == 'POST':
        notes_serializer = NoteSerializer(data=request.data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return Response(notes_serializer.data,
                            status=status.HTTP_201_CREATED)
    return Response(notes_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        note_serializer = Note(note)
        return Response(note_serializer.data)
    elif request.method == 'PUT':
        note_serializer = NoteSerializer(note_serializer, data=request.data)
        if note_serializer.is_valid():
            note_serializer.save()
            return Response(note_serializer.data)
        return Response(note_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
