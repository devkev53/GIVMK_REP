from .views import CustomerListView, ClientCreateView
from django.urls import path, include

urlpatterns = [
    path('customersList/', CustomerListView.as_view(), name='customersList' ),
    path('addClient/', ClientCreateView.as_view(), name='addClient' ),
]