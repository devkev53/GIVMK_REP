from .views import PedidosListView, PedidooDeleteView
# from .views import ClientUpdateView, ClientDetailView
from django.urls import path, include

urlpatterns = [
    path('pedidosList/', PedidosListView.as_view(), name='pedidosList' ),
    # path('addClient/', ClientCreateView.as_view(), name='addClient' ),
    path('deletePedido/<int:pk>/', PedidooDeleteView.as_view(), name='deletePedido' ),
    # path('updateClient/<int:pk>/', ClientUpdateView.as_view(), name='updateClient' ),
    # path('detailClient/<int:pk>/', ClientDetailView.as_view(), name='detailClient' ),
]