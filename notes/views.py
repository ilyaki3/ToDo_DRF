from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Project, Note
from .serializers import ProjectSerializer, NoteSerializer


# Create your views here.
class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class NoteModelViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
