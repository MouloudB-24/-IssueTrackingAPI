from django.urls import path, include
from rest_framework.routers import SimpleRouter

from projects.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet

router = SimpleRouter()
router.register("projects", ProjectViewSet, basename="Projects")
router.register("contributions", ContributorViewSet, basename="contributions")
router.register("issues", IssueViewSet, basename="Issues")
router.register("comments", CommentViewSet, basename="Comments")

urlpatterns = [
    path('', include(router.urls)),
]