from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Contributor
from projects.serializers import ProjectSerializer, ContributorSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()


