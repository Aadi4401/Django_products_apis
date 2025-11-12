from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    admin role has full access; 'user' role only read.
    """

    def has_permission(self, request, view):
        # Allow safe methods for everyone with token (default permission requires authentication)
        if request.method in permissions.SAFE_METHODS:
            return True
        # For non-safe methods require admin role
        profile = getattr(request.user, "profile", None)
        if profile and profile.role == "admin":
            return True
        return False
