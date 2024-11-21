from django.urls import path, include
from rest_framework.routers import SimpleRouter

from issues.views import IssueViewSet, CommentViewSet

router = SimpleRouter()
router.register("issues", IssueViewSet, basename="Issues")
router.register("comments", CommentViewSet, basename="Comments")

urlpatterns = [
    path('', include(router.urls))
]
