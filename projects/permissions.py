from rest_framework.permissions import BasePermission, SAFE_METHODS

from projects.models import Contribution

import logging
logger = logging.getLogger(__name__)


class IsAuthorOrReadOnly(BasePermission):
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


class IsIssueParticipant(BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_pk')
        is_participant = Contribution.objects.filter(project_id=project_id, user=request.user).exists()
        logger.debug(f"User {request.user} - is participant: {is_participant}")
        return is_participant

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            logger.debug(f"SAFE_METHODS: {request.method} - Granted to {request.user}")
            return True

        is_author = obj.author == request.user
        logger.debug(f"Object author: {obj.author}, Request user: {request.user} - is_author: {is_author}")
        return is_author


class IsCommentProjectParticipant(BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_pk')
        return Contribution.objects.filter(project_id=project_id, user=request.user).exists()



