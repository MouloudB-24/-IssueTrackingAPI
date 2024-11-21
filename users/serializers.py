from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'can_be_contacted', 'can_data_be_shared', 'time_created']

    def validate_age(self, value):
        if value < 15:
            raise serializers.ValidationError("Users must be at least 15 years old.")
        return value
