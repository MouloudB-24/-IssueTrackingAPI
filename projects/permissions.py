from rest_framework.permissions import BasePermission, SAFE_METHODS

from projects.models import Contribution


class IsAuthorProjectOrReadOnly(BasePermission):
    """
    Permission that gives full access to the author of a resource and Read-only access to the other users.
    """
    def has_object_permission(self, request, view, obj):
        contribution = obj.contributions.filter(user=request.user).first()

        if not contribution:
            return False

        # If it's reading method (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return contribution.role in ["AUTHOR", "CONTRIBUTOR"]

        # For methods (POST, PUT, DELETE) only author can modify
        return contribution.role == "AUTHOR"


class IsAuthorIssueOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_pk')
        return Contribution.objects.filter(project_id=project_id, user=request.user).exists()

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAuthorCommentOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_pk')
        return Contribution.objects.filter(project_id=project_id, user=request.user).exists()

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
