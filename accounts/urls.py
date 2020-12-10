from django.urls import path

from accounts import views

urlpatterns = [
    path('user/list/', views.UserList.as_view(), name='user_list'),
    path('user/register/', views.UserRegister.as_view(), name='user_register'),
]
