from rest_framework import serializers

from mocks.models import Mock


class MockSerializer(serializers.ModelSerializer):
    """
    DRF serializer to represent mock model.
    """
    class Meta:
        model = Mock
        fields = ('type', 'payload',)
