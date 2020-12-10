from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

from accounts.models import User
from accounts.serializers import UserSerializer

# TODO: CRUD User


class UserList(generics.ListAPIView):
    """
    Lists of all users
    endpoint: /api/v1/accounts/users/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserRegister(generics.CreateAPIView):
    """
    Creates a new user
    endpoint: /api/v1/accounts/user/
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# TODO: CRUD Profile
