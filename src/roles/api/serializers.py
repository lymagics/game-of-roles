from rest_framework import serializers

from roles.models import IntervalChoices, Role


class RoleSerializer(serializers.ModelSerializer):
    """
    DRF serializer to represent role.
    """
    class Meta:
        model = Role
        fields = ('name', 'description', 'price_per_month',)


class CheckoutSerializer(serializers.Serializer):
    """
    DRF serializer to represent chekout.
    """
    name = serializers.CharField()
    interval = serializers.ChoiceField(choices=IntervalChoices, write_only=True)
    url = serializers.URLField(read_only=True)
