from rest_framework.serializers import ModelSerializer
from issues.models import Issue, Comment


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ["id", "title", "description", "status", "priority", "tag", "time_created", "time_updated", "project",
                  "author", "assignee"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "time_created", "issue", "author"]
