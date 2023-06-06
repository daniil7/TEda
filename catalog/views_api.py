from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from catalog.serializers import UserSerializer, GroupSerializer


class IsAdminPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser

class IsStaffPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAdminPermissions]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminPermissions]
