from django.shortcuts import get_object_or_404

from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from core.permissions import IsRegular
from roles.api.serializers import CheckoutSerializer, RoleSerializer
from roles.models import Role


class RoleViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTCookieAuthentication,)

    def get_queryset(self):
        return Role.objects.all()

    @extend_schema(
        request=CheckoutSerializer,
        responses=CheckoutSerializer,
    )
    @action(detail=False,
            methods=('post',),
            permission_classes=(IsRegular,))
    def purchase(self, request: Request):
        serializer = CheckoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        role_name = serializer.validated_data.get('name')
        role = get_object_or_404(Role, name=role_name)

        interval = serializer.validated_data.get('interval')
        url = role.to_checkout(request.user, interval)

        serializer.validated_data['url'] = url
        return Response(serializer.data, status=200)
