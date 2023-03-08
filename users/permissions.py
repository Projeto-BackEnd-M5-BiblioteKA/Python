from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return request.user.is_authenticated and obj == request.user
