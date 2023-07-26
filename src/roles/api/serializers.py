from rest_framework import serializers

from roles.models import Role


class RoleSerializer(serializers.ModelSerializer):
    """
    DRF serializer to represent role.
    """
    class Meta:
        model = Role
        fields = ('name', 'description', 'price_per_month',)
