from .views import ProductosListView, ProductoCreateView, ProductoDeleteView
from .views import ProductoUpdateView, ProductoDetailView
from django.urls import path, include

urlpatterns = [
    path('productosList/', ProductosListView.as_view(), name='productosList' ),
    path('addProducto/', ProductoCreateView.as_view(), name='addProducto' ),
    path('deleteProducto/<int:pk>/', ProductoDeleteView.as_view(), name='deleteProducto' ),
    path('updateProducto/<int:pk>/', ProductoUpdateView.as_view(), name='updateProducto' ),
    path('detailProducto/<int:pk>/', ProductoDetailView.as_view(), name='detailProducto' ),
]