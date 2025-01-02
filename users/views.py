from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserListSerializer, UserDetailSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserListSerializer
    detail_serializer_class = UserDetailSerializer
    queryset = User.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]

    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'create']:
            return self.detail_serializer_class
        return super().get_serializer_class()

