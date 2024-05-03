from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """ Класс разрешения который позволяет просматривать всем, а удалять только админам"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)
