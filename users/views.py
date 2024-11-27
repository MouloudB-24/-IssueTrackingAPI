from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserListSerializer, UserDetailSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserListSerializer
    detail_serializer_class = UserDetailSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()





