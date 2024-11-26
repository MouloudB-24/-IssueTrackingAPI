from rest_framework.serializers import ModelSerializer

from projects.models import Project, Contribution, Issue, Comment


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contribution
        fields = ["id", "user", "project", "role"]


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ["id", "title", "description", "status", "priority", "tag", "time_created", "time_updated", "project",
                  "author", "assignee"]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "time_created", "issue", "author"]


class ProjectSerializer(ModelSerializer):
    issues = IssueSerializer(many=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "type", "author", "time_created", "issues", "comments"]

    #def save(self, **kwargs):
        #import ipdb; ipdb.set_trace()
        #return super().save(**kwargs)




