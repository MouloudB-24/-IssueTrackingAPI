from django.contrib import admin
from projects.models import Project, Contribution, Issue, Comment

admin.site.register(Project)
admin.site.register(Contribution)
admin.site.register(Issue)
admin.site.register(Comment)
