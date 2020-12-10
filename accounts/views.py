from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from accounts.models import User, UserProfile, EmployerProfile
from accounts.serializers import UserSerializer, UserProfileSerializer, EmployerProfileSerializer


class UserListAPI(generics.ListAPIView):
    """
    Lists of all users
    endpoint: /api/v1/accounts/users/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserRegisterAPI(generics.CreateAPIView):
    """
    Creates a new user
    endpoint: /api/v1/accounts/user/
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserProfileAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    is_employer = False

    def __init__(self, is_employer=False, *args, **kwargs):
        super(UserProfileAPI, self).__init__(*args, **kwargs)
        if is_employer:
            self.serializer_class = EmployerProfileSerializer
            self.model_class = EmployerProfile
        else:
            self.serializer_class = UserProfileSerializer
            self.model_class = UserProfile

    def get_object(self):
        return get_object_or_404(self.model_class, pk=self.kwargs.get('pk', -1))

    def update(self, request, *args, **kwargs):
        profile_object = self.get_object()
        if profile_object.user == self.request.user:
            return super(UserProfileAPI, self).update(request, *args, **kwargs)
        else:
            return Response({'detail': 'Permission Denied.'}, status=status.HTTP_401_UNAUTHORIZED)
