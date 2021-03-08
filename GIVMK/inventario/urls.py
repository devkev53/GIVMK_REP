from .views import CustomerListView, ClientCreateView, ClientDeleteView
from .views import ClientUpdateView, ClientDetailView
from django.urls import path, include

urlpatterns = [
    path('customersList/', CustomerListView.as_view(), name='customersList' ),
    path('addClient/', ClientCreateView.as_view(), name='addClient' ),
    path('deleteClient/<int:pk>/', ClientDeleteView.as_view(), name='deleteClient' ),
    path('updateClient/<int:pk>/', ClientUpdateView.as_view(), name='updateClient' ),
    path('detailClient/<int:pk>/', ClientDetailView.as_view(), name='detailClient' ),
]