from django.urls import path, include
from rest_framework.routers import SimpleRouter

from users.views import UserViewSet

router = SimpleRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls))
]