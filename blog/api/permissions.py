
from rest_framework import permissions


class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.author

class IsAdminUserForObject(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)
    
    '''
        This is the same reason our AuthorModifyOrReadOnly inherited from
        IsAuthenticatedOrReadOnly instead of BasePermission. We want to use
        IsAuthenticatedOrReadOnly’s has_permission() method and only
        implement our own has_object_permission() method.
    '''
