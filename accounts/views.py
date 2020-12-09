from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

from accounts.models import User
from accounts.serializers import UserSerializer


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

    def get(self, *args, **kwargs):
        """
        endpoint: /api/v1/accounts/user/
        :return: Response object includes authenticated user info or 401 message
        """
        if self.request.user.is_authenticated:
            return Response(
                data=UserSerializer(instance=self.request.user).data
            )
        else:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_401_UNAUTHORIZED)
