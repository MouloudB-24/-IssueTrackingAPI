from django.urls import path, include
from rest_framework.routers import SimpleRouter

from projects.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet

router = SimpleRouter()
router.register("projects", ProjectViewSet, basename="projects")
router.register("contributions", ContributorViewSet, basename="contributions")
router.register("issues", IssueViewSet, basename="issues")
router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [
    path('', include(router.urls)),
]