from django.urls import path

from jobs import views

urlpatterns = [
    path('opportunity/<int:pk>/', views.OpportunityAPI.as_view(), name='opportunity'),
]
