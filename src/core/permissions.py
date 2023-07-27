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


class IsPremium(BaseIsRole):
    """
    Allow only permium player to access.
    """
    role = 'Premium'


class IsExtra(BaseIsRole):
    """
    Allow only extra player to access.
    """
    role = 'Extra'


class IsLuxe(BaseIsRole):
    """
    Allow only luxe player to access.
    """
    role = 'Luxe'
