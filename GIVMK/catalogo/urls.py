from .views import ProductosListView, ProductoCreateView
# from .views import ClientUpdateView, ClientDetailView
from django.urls import path, include

urlpatterns = [
    path('productosList/', ProductosListView.as_view(), name='productosList' ),
    path('addProducto/', ProductoCreateView.as_view(), name='addProducto' ),
    # path('deleteClient/<int:pk>/', ClientDeleteView.as_view(), name='deleteClient' ),
    # path('updateClient/<int:pk>/', ClientUpdateView.as_view(), name='updateClient' ),
    # path('detailClient/<int:pk>/', ClientDetailView.as_view(), name='detailClient' ),
]