from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, HyperlinkedModelSerializer

from authapp.serializers import UserSerializer
from .models import Project, Note


class ProjectSerializer(ModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ('name', 'repository_link', 'users')


# class NoteSerializer(HyperlinkedModelSerializer):
class NoteSerializer(ModelSerializer):
    user = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = Note
        fields = ('project', 'text', 'created_at', 'updated_at', 'user', 'is_active')
