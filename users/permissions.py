from rest_framework import permissions
from rest_framework.views import Request
from .models import User


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, req: Request, view, obj: User):
        if req.method == permissions.SAFE_METHODS and req.user.is_authenticated:
            return True
        return req.user.username == obj.username or req.user.is_superuser
