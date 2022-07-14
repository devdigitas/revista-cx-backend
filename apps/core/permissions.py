from rest_framework import permissions


class PlayerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else: 
            return True

    def has_object_permission(self, request, view, obj):
        is_admin = request.user.is_admin
        is_staff = request.user.is_staff
        is_superuser = request.user.is_superuser

        if is_admin or is_staff or is_superuser:
            return True
        else:
            return request.user == obj.team.manager