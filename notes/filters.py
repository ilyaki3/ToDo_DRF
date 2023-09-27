from django_filters import DateFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import FilterSet, CharFilter
from notes.models import Project, Note
from notes.serializers import ProjectSerializer


class ProjectParamFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        projects = Project.objects.all()

        if name:
            projects = projects.filter(name__contains=name)
        return projects


class NotesFilter(FilterSet):
    project__name = CharFilter(lookup_expr='contains')
    created_at__gte = DateFilter(field_name='created_at', lookup_expr='gte', label='Дата начала')
    created_at__lte = DateFilter(field_name='created_at', lookup_expr='lte', label='Дата окончания')

    class Meta:
        model = Note
        fields = ['project__name', 'created_at__gte', 'created_at__lte']
