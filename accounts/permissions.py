from rest_framework.permissions import BasePermission


class IsUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            if request.user.is_authenticated:
                return not request.user.is_employer
            return False


class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_employer
