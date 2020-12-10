from django.urls import path

from accounts import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/list/', views.UserListAPI.as_view(), name='user_list'),
    path('user/register/', views.UserRegisterAPI.as_view(), name='user_register'),
    path('user/profile/<int:pk>/', views.UserProfileAPI.as_view(), name='user_profile'),
    path('employer/profile/<int:pk>/', views.UserProfileAPI.as_view(is_employer=True), name='employer_profile')
]
