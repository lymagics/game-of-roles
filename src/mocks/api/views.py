from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsPremium, IsExtra, IsLuxe
from mocks.api.serializers import MockSerializer
from mocks.models import Mock


class MockViewSet(mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = MockSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTCookieAuthentication,)
    queryset = Mock.objects.all()


class PhoneMockViewSet(MockViewSet):
    permission_classes = MockViewSet.permission_classes + (IsPremium,)

    def get_object(self):
        return Mock.objects.filter(type='phone_number').first()


class ColorMockViewSet(MockViewSet):
    permission_classes = MockViewSet.permission_classes + (IsExtra,)

    def get_object(self):
        return Mock.objects.filter(type='color').first()


class PassportMockViewSet(MockViewSet):
    permission_classes = MockViewSet.permission_classes + (IsLuxe,)

    def get_object(self):
        return Mock.objects.filter(type='passport_number').first()
