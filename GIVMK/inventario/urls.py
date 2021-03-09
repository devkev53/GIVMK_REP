from .views import PedidosListView
# from .views import ClientUpdateView, ClientDetailView
from django.urls import path, include

urlpatterns = [
    path('pedidosList123/', PedidosListView.as_view(), name='pedidosList' ),
    # path('addClient/', ClientCreateView.as_view(), name='addClient' ),
    # path('deleteClient/<int:pk>/', ClientDeleteView.as_view(), name='deleteClient' ),
    # path('updateClient/<int:pk>/', ClientUpdateView.as_view(), name='updateClient' ),
    # path('detailClient/<int:pk>/', ClientDetailView.as_view(), name='detailClient' ),
]