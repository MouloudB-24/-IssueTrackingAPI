from rest_framework.viewsets import ModelViewSet

from issues.models import Issue, Comment
from issues.serializers import IssueSerializer, CommentSerializer


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

