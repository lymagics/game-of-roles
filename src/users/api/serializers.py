from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    DRF serializer to represent user model.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 
                  'about_me',)
        read_only_fields = ('id',)
