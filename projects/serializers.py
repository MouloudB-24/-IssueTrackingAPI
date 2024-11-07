from rest_framework.serializers import ModelSerializer
from projects.models import Project, Contributor


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description", "type", "author", "time_created"]


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "role"]
