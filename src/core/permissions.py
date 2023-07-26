from rest_framework import permissions


class BaseIsRole(permissions.BasePermission):
    """
    Base permission for role based access.
    """
    @property
    def role(self):
        raise NotImplementedError
    
    def has_permission(self, request, view):
        """
        Check user role is premium.
        """
        return request.user.subscriptions.filter(role__name=self.role).exists()


class IsPremium(permissions.BasePermission):
    """
    Allow only permium player to access.
    """
    role = 'Premium'


class IsExtra(permissions.BasePermission):
    """
    Allow only extra player to access.
    """
    role = 'Extra'


class IsLuxe(permissions.BasePermission):
    """
    Allow only luxe player to access.
    """
    role = 'Luxe'
