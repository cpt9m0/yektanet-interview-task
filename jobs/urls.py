from django.urls import path

from jobs import views

urlpatterns = [
    path('opportunity/<int:pk>/', views.OpportunityAPI.as_view(), name='opportunity'),
    path('opportunities/', views.OpportunityListCreateAPI.as_view(), name='opportunity_list_create'),
    path('opportunity/search/', views.OpportunitySearchListAPI.as_view(), name='opportunity_search'),
]
