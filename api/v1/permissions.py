from rest_framework.permissions import BasePermission


class IsAdminOrIsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated) and (
            obj.user == request.user or request.user.is_staff
        )
