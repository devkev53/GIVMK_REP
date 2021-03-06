from .views import CustomerListView, ClientCreateView, ClientDeleteView
from django.urls import path, include

urlpatterns = [
    path('customersList/', CustomerListView.as_view(), name='customersList' ),
    path('addClient/', ClientCreateView.as_view(), name='addClient' ),
    path('deleteClient/<int:pk>/', ClientDeleteView.as_view(), name='deleteClient' ),
]