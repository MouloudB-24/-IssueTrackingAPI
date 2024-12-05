from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from projects.models import Project, Contribution, Issue, Comment
from users.serializers import UserListSerializer


# ----- Projects ------
class ProjectSerializer(ModelSerializer):
    #issues = IssueDetailSerializer(many=True, read_only=True)
    #contributions = ContributionsSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "type", "time_created"]
        #read_only_fields = ["author"]


# ----- Contributions ------
class ContributionsSerializer(ModelSerializer):

    class Meta:
        model = Contribution
        fields = ["id", "user", 'project', "role"]
        read_only_fields = ['project']


# ----- Issues ------
class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ["id", "title", "description", "status"]


class IssueDetailSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ["id", "title", "description", "status", "priority", "tag", "time_created", "time_updated", "project",
                  "author", "assignee"]


# ----- Comments ------
class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ["id", "content", "time_created", "issue", "author"]


