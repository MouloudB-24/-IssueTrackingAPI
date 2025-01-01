from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from projects.models import Project, Contribution, Issue, Comment


# ----- Projects ------
class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ["id", "name", "description", "type", "author", "time_created"]
        read_only_fields = ["author"]


# ----- Contributions ------
class ContributionsSerializer(ModelSerializer):

    class Meta:
        model = Contribution
        fields = ["id", "user", 'project', "role"]
        read_only_fields = ['project', 'role']


# ----- Issues ------
class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ["id", "title", "description", "status"]


class IssueDetailSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ["id", "title", "description", "status", "priority", "tag", "time_created", "time_updated", "project",
                  'author', "assignee"]
        read_only_fields = ['author', 'project']
        extra_kwargs = {'assignee': {'required': True}}

    def validate_assignee(self, value):
        # Get current project ID
        project = self.context['view'].kwargs.get('project_pk')

        if not Contribution.objects.filter(project=project, user=value).exists():
            raise serializers.ValidationError(f"User {value} is not a contributor to project {project}.")

        return value


# ----- Comments ------
class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ["id", "content", "time_created", "issue", "author"]
        read_only_fields = ['issue', 'author']


