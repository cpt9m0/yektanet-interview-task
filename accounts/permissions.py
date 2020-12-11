from rest_framework.permissions import BasePermission


class OpportunityPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            """
            Both employer and user can view opportunities.
            """
            return True
        elif request.method == 'POST':
            """
            Just a user can request for an opportunity
            """
            return not request.user.is_employer
        elif request.method == 'PUT' or request.method == 'PATCH':
            """
            Just an employer can edit its opportunity
            """
            return request.user.is_employer
        else:
            return False


class IsEmployerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_employer
