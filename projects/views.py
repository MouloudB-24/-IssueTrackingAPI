from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

import projects.serializers as ps
from projects.models import Project, Contribution, Issue, Comment
from projects.permissions import IsAuthorProjectOrReadOnly, IsAuthorIssueOrReadOnly, IsAuthorCommentOrReadOnly
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.generics import RetrieveUpdateDestroyAPIView


# ----- Projects ------
class ProjectViewSet(ModelViewSet):
    serializer_class = ps.ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorProjectOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Project.objects.filter(contributions__user=self.request.user).distinct()
        return Project.objects.none()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# ----- Contributions ------
class ProjectContributionsView(ListCreateAPIView):
    serializer_class = ps.ContributionsSerializer
    permission_classes = [IsAuthenticated, IsAuthorProjectOrReadOnly]

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

            if not project.contributions.filter(user=self.request.user, role="AUTHOR").exists():
                raise PermissionDenied("Only project author can add contributors.")

            serializer.save(project=project)

        except Project.DoesNotExist:
            raise NotFound(f"Project {project_id} not found")


class ProjectIssuesView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAuthorIssueOrReadOnly]

    def get_queryset(self):
        # Filter issues by project
        project_id = self.kwargs.get('project_pk')
        return Issue.objects.filter(project_id=project_id)

    def get_serializer_class(self):
        return ps.IssueListSerializer

    def perform_create(self, serializer):
        # Associate issue with project
        project_id = self.kwargs.get('project_pk')

        try:
            project = Project.objects.get(id=project_id)
            serializer.save(project=project, author=self.request.user)

        except Project.DoesNotExist:
            raise NotFound(f"Project {project_id} not found.")


class ProjectIssueInstanceView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorIssueOrReadOnly]
    serializer_class = ps.IssueDetailSerializer

    def get_object(self):
        project_id = self.kwargs.get('project_pk')
        issue_id = self.kwargs.get('issue_pk')
        try:
            issue = Issue.objects.get(project_id=project_id, id=issue_id)

        except Issue.DoesNotExist:
            raise NotFound(f"Issue {issue_id} not found in project {project_id}")

        self.check_object_permissions(self.request, issue)
        return issue


class ProjectIssueCommentsView(ListCreateAPIView):
    serializer_class = ps.CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorCommentOrReadOnly]

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


class ProjectIssueCommentInstanceView(RetrieveUpdateDestroyAPIView):
    serializer_class = ps.CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorCommentOrReadOnly]

    def get_object(self):
        issue_id = self.kwargs.get('issue_pk')
        comment_id = self.kwargs.get('comment_pk')

        try:
            comment = Comment.objects.get(issue_id=issue_id, id=comment_id)

        except Comment.DoesNotExist:
            raise NotFound(f"Comment {comment_id} not found in issue {issue_id}")

        self.check_object_permissions(self.request, comment)
        return comment




