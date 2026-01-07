from rest_framework import permissions


class IsAdminOrModeratorOrProfileOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__in=['Администратор', 'Модератор']).exists():
                return True

        return request.user == view.get_object()


class IsAdminOrProfileOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Администратор').exists():
                return True

        return request.user == view.get_object()


class IsAdminOrModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__in=['Администратор', 'Модератор']).exists():
                return True


class IsProfileOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user == view.get_object()


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
