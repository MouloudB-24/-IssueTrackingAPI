from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, ValidationError
from users.models import User


class UserListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name="users-detail")

    class Meta:
        model = User
        fields = ['id', 'username', 'url']


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'can_be_contacted', 'can_data_be_shared', 'time_created']

    def validate_age(self, value):
        if value < 15:
            raise ValidationError("Users must be at least 15 years old.")
        return value
