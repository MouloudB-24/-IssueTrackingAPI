from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from projects.models import Project, Contribution, Issue, Comment
from users.serializers import UserListSerializer


# ----- Projects ------
class ProjectSerializer(ModelSerializer):
    #issues = IssueSerializer(many=True, read_only=True)
    #contributions = ContributionsSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "type", "author", "time_created"]


# ----- Contributions ------
class ContributionsSerializer(ModelSerializer):

    class Meta:
        model = Contribution
        fields = ["id", "user", 'project', "role"]
        read_only_fields = ['project']


# ----- Issues ------
class IssueSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ["id", "title", "description", "status", "priority", "tag", "time_created", "time_updated", "project",
                  "author", "assignee"]


# ----- Comments ------
class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ["id", "content", "time_created", "issue", "author"]


