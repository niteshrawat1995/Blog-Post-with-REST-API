from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    message = 'You must be the author of the post.'

    def has_object_permission(self, request, view, obj):
        SAFE_METHODS = ['GET']
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

