from django.urls import path

from accounts import views

urlpatterns = [
    path('user/list/', views.UserListAPI.as_view(), name='user_list'),
    path('user/register/', views.UserRegisterAPI.as_view(), name='user_register'),
    path('user/profile/<int:pk>/', views.UserProfileAPI.as_view(), name='user_profile'),
    path('employer/profile/<int:pk>/', views.UserProfileAPI.as_view(is_employer=True), name='employer_profile')
]
