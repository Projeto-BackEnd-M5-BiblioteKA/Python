from rest_framework.permissions import BasePermission


class CustomLoansPermissions(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        if request.method != "GET":
            return request.user.is_superuser

        return request.user.is_authenticated
