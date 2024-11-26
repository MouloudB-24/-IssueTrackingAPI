from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Contribution, Issue, Comment
from projects.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contribution.objects.all()


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()



