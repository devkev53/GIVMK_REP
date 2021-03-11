from .views import PedidosListView, PedidoDeleteView, PedidoCreate
# from .views import ClientUpdateView, ClientDetailView
from django.urls import path, include

urlpatterns = [
    path('pedidosList/', PedidosListView.as_view(), name='pedidosList' ),
    path('addPedido/', PedidoCreate.as_view(), name='addPedido' ),
    path('deletePedido/<int:pk>/', PedidoDeleteView.as_view(), name='deletePedido' ),
    # path('updateClient/<int:pk>/', ClientUpdateView.as_view(), name='updateClient' ),
    # path('detailClient/<int:pk>/', ClientDetailView.as_view(), name='detailClient' ),
]