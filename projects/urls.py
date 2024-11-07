from django.urls import path, include
from rest_framework.routers import DefaultRouter

from projects.views import ProjectViewSet, ContributorViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="Projects")
router.register(r"contributors", ContributorViewSet, basename="contributors")


urlpatterns = [
    path('', include(router.urls))
]