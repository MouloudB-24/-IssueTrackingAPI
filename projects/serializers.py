from rest_framework.serializers import ModelSerializer

from issues.serializers import IssueSerializer
from projects.models import Project, Contribution


class ProjectSerializer(ModelSerializer):
    issues = IssueSerializer(many=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "type", "author", "time_created", "issues"]


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contribution
        fields = ["id", "user", "project", "role"]



