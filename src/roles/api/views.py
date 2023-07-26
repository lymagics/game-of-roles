from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from roles.api.serializers import RoleSerializer
from roles.models import Role


class RoleViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = RoleSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTCookieAuthentication,)

    def get_queryset(self):
        return Role.objects.all()
