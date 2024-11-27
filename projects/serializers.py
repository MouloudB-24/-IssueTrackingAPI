from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from projects.models import Project, Contribution, Issue, Comment
from users.serializers import UserListSerializer


# -----1. Contributions ------
class ContributionsSerializer(ModelSerializer):
    user = UserListSerializer()
    project = SerializerMethodField()

    class Meta:
        model = Contribution
        fields = ["id", "user", "project", "role"]

    def get_project(self, obj):
        return {'id': obj.project.id, 'name': obj.project.name}


# -----2. Issues ------
class IssueListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='issues-detail')

    class Meta:
        model = Issue
        fields = ['id', 'title', 'url']


class IssueDetailSerializer(ModelSerializer):
    author = UserListSerializer()
    assignee = UserListSerializer()
    project = SerializerMethodField()

    class Meta:
        model = Issue
        fields = ["id", "title", "description", "status", "priority", "tag", "time_created", "time_updated", "project",
                  "author", "assignee"]

    def get_project(self, obj):
        return {'id': obj.project.id, 'name': obj.project.name}


# -----3. Comments ------
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "time_created", "issue", "author"]


class ProjectListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name="projects-detail")

    class Meta:
        model = Project
        fields = ["id", "name", "time_created", "url"]


# -----4. Projects ------
class ProjectDetailSerializer(ModelSerializer):
    issues = IssueListSerializer(many=True)
    contributions = ContributionsSerializer(many=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "type", "time_created", "issues", "contributions"]





