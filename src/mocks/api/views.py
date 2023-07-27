from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from core.permissions import IsPremium, IsExtra, IsLuxe
from mocks.api.serializers import MockSerializer
from mocks.models import Mock


class MockViewSet(viewsets.GenericViewSet):
    serializer_class = MockSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTCookieAuthentication,)
    queryset = Mock.objects.all()

    @action(detail=False, 
            methods=('get',),
            permission_classes=(IsPremium,))
    def phone(self, request: Request):
        obj = Mock.objects.filter(type='phone_number').first()
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=200)

    @action(detail=False, 
            methods=('get',),
            permission_classes=(IsExtra,))
    def color(self, request: Request):
        obj = Mock.objects.filter(type='color').first()
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=200)

    @action(detail=False, 
            methods=('get',),
            permission_classes=(IsLuxe,))
    def passport(self, request: Request):
        obj = Mock.objects.filter(type='passport_number').first()
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=200)
