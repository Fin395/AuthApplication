from rest_framework import permissions


class IsAdminOrModeratorOrProfileOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__in=['Администратор', 'Модератор']).exists():
            return request.user.has_perm('users.delete_user')

        return request.user == view.get_object()


class IsAdminOrProfileOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Администратор').exists():
            return request.user.has_perm('users.change_user')

        return request.user == view.get_object()


class IsAdminOrModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name__in=['Администратор', 'Модератор']).exists():
            return request.user.has_perm('users.view_user')
