from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Permission that gives full access to the author of a resource and Read-only access to the other users.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsContributor(BasePermission):
    """
    Permission that gives access to the contributors of a project.
    """

    def has_object_permission(self, request, view, obj):
        return request.user in obj.project.contributions.all()



