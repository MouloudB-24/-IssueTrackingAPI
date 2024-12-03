from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

import projects.serializers as ps
from projects.models import Project, Contribution, Issue, Comment
from projects.permissions import IsAuthorOrReadOnly, IsContributor
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class ProjectViewSet(ModelViewSet):
    serializer_class = ps.ProjectSerializer
    queryset = Project.objects.all()
    #permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    """def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "create" or self.action == "update":
            return self.detail_serializer_class
        return super().get_serializer_class()"""


# ----- Contributions ------
class ProjectContributionsView(ListCreateAPIView):
    serializer_class = ps.ContributionsSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Contribution.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        try:
            project = Project.objects.get(id=project_id)

            user_to_add = serializer.validated_data['user']
            if Contribution.objects.filter(project=project, user=user_to_add).exists():
                raise ValueError("This use is already a contributor to this project")

            serializer.save(project=project)

        except Project.DoesNotExist:
            raise NotFound(f"Project {project_id} not found")


class ProjectIssuesView(ListCreateAPIView):
    serializer_class = ps.IssueSerializer
    #permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        # Filter issues by project
        project_id = self.kwargs.get('project_pk')
        return Issue.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        # Associate issue with project
        project_id = self.kwargs.get('project_pk')
        serializer.save(project_id=project_id)


class ProjectIssueDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ps.IssueSerializer

    def get_object(self):
        project_id = self.kwargs.get('project_pk')
        issue_id = self.kwargs.get('issue_pk')
        try:
            return Issue.objects.get(project_id=project_id, id=issue_id)
        except Issue.DoesNotExist:
            raise NotFound(f"Issue {issue_id} not found in project {project_id}")


class ProjectIssueCommentsView(ListCreateAPIView):
    serializer_class = ps.CommentSerializer

    def get_queryset(self):
        # Filter comments by issue
        issue_id = self.kwargs.get('issue_pk')
        return Comment.objects.filter(issue_id=issue_id)

    def perform_create(self, serializer):
        # Associate comment with issue
        project_id = self.kwargs.get('project_pk')
        issue_id = self.kwargs.get('issue_pk')
        try:
            issue = Issue.objects.get(project_id=project_id, id=issue_id)
        except Issue.DoesNotExist:
            raise NotFound(f"Issue {issue_id} not found in project {project_id}")

        serializer.save(issue=issue)


class ProjectIssueCommentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ps.CommentSerializer

    def get_object(self):
        issue_id = self.kwargs.get('issue_pk')
        comment_id = self.kwargs.get('comment_pk')

        try:
            return Comment.objects.get(issue_id=issue_id, id=comment_id)

        except Comment.DoesNotExist:
            raise NotFound(f"Comment {comment_id} not found in issue {issue_id}")
