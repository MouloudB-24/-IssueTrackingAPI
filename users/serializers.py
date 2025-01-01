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
        fields = ['id', 'username', 'password', 'email', 'age', 'can_be_contacted', 'can_data_be_shared', 'time_created']
        extra_kwargs = {
            "password": {"write_only": True},
            "age": {"required": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User.objects.create_user(**validated_data)

        if password:
            user.set_password(password)
        user.save()
        return user

    def validate_age(self, value):
        if value < 15:
            raise ValidationError("Users must be at least 15 years old.")
        return value
