from rest_framework import permissions

class UserPermission(permissions.BasePermission):

    message = "This object is expired." 
    # code = 
    def has_permission(self, request, view):
        admin_users = ['is_admin', 'is_operative', 'is_resultLogger', 'is_staff', 'is_superuser']

        if not request.user.is_anonymous:
            return True
        else:
            if request.method == 'POST':
                data = request.data
                for admin_user in admin_users:
                    if data.get(admin_user):
                        return False
                return True
            else:
                return False


class MangerPermission(permissions.BasePermission):

    message = "This object is expired." 
    # code = 
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            if request.method == 'POST':
                return True
            else:
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
            return request.user == obj.user