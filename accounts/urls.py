from django.urls import path

from accounts import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('user/', views.UserRegister.as_view(), name='user'),
]
