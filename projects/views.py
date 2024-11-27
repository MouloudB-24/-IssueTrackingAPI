from rest_framework.viewsets import ModelViewSet

import projects.serializers as ps
from projects.models import Project, Contribution, Issue, Comment


class ProjectViewSet(ModelViewSet):
    serializer_class = ps.ProjectListSerializer
    detail_serializer_class = ps.ProjectDetailSerializer
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContributorViewSet(ModelViewSet):
    serializer_class = ps.ContributionsSerializer
    queryset = Contribution.objects.all()


class IssueViewSet(ModelViewSet):
    serializer_class = ps.IssueListSerializer
    detail_serializer_class = ps.IssueDetailSerializer
    queryset = Issue.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class CommentViewSet(ModelViewSet):
    serializer_class = ps.CommentSerializer
    queryset = Comment.objects.all()



