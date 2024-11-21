from django.core.exceptions import ValidationError
from django.db import models

from issuetracking.settings import AUTH_USER_MODEL
from projects.models import Project, Contributor


class Issue(models.Model):
    STATUS_CHOICES = (("TODO", "To Do"),
                      ("INPROGRESS", "In Progress"),
                      ("FINISHED", "Finished"))

    PRIORITY_CHOICES = (("LOW", "Low"),
                        ("MEDIUM", "Medium"),
                        ("HIGH", "High"))

    TAG_CHOICES = (("BUG", "Bug"),
                   ("FEATURE", "Feature"),
                   ("TASK", "Task"))

    title = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.CharField(max_length=20, choices=TAG_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="TODO")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name="issues")
    author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="authored_issues")
    assignee = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="contributed_issues")
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"

    """def clean(self):
        if self.project.author != self.author:
            print(self.project.author, self.author)

            raise ValidationError("L'auteur de l'issue doit être un contributeur ou auteur de projet")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)"""


class Comment(models.Model):
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name="Comments")
    author = models.ForeignKey(to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Comments")
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.issue.title}"
