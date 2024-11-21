from django.urls import path, include
from rest_framework.routers import SimpleRouter

from projects.views import ProjectViewSet, ContributorViewSet

router = SimpleRouter()
router.register("projects", ProjectViewSet, basename="Projects")
router.register("contributors", ContributorViewSet, basename="contributors")

urlpatterns = [
    path('', include(router.urls))
]