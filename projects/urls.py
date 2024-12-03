from django.urls import path, include
from rest_framework.routers import SimpleRouter

from projects.views import ProjectViewSet

router = SimpleRouter()
router.register('', ProjectViewSet, basename="projects")

urlpatterns = [
    path('', include(router.urls)),
]