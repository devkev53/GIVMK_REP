import json

from catalogo.forms import ProductoForm
from catalogo.models import Producto
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .models import Pedido, DetallePedido
from .forms import PedidoForm

# Create your views here.

class PedidosListView(ListView):

    model = Pedido
    template_name = 'inventario/pedidos_list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Pedido.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Listado de Pedidos')
        return context

class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = reverse_lazy('pedidosList')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class PedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy('pedidosList')
    url_redirect = success_url

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            # prod = Producto.objects.filter(id=request.POST['id']).get()
            if action == 'autocomplete':
                data = []
                for i in Producto.objects.filter(nombre__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.nombre
                    print(i.nombre)
                    data.append(item)
            elif action == 'crearProd':
                with transaction.atomic():
                    if request.FILES:
                        formProd = ProductoForm(request.POST, request.FILES)
                    else:
                        formProd = ProductoForm(request.POST)
                    formProd.is_valid()
                    # Recuperamos la data del cliente guardado
                    data = formProd.save()
            elif action == 'add':
                with transaction.atomic():
                    requestPedido = json.loads(request.POST['ingr'])
                    nuevoPedido = Pedido()
                    nuevoPedido.fecha = requestPedido['fecha']
                    nuevoPedido.referencia = requestPedido['referencia']
                    nuevoPedido.totalConsultora = float(requestPedido['totalConsultora'])
                    nuevoPedido.totalCatalogo = float(requestPedido['totalCatalogo'])
                    nuevoPedido.save()

                    for i in requestPedido['productos']:
                        det = DetallePedido()
                        det.pedido = nuevoPedido
                        det.producto = Producto.objects.filter(id=i['id']).get()
                        det.pConsultora = float(i['precio_consultora'])
                        det.pCatalogo = float(i['precio_catalogo'])
                        det.cantidad = int(i['cantidad'])
                        det.save()
            else:
                data['error'] = 'No ha ingresado a Ninguna Opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'add'
        context['titulo'] = _('Registrar Pedido')
        context['lazyUrl'] = self.url_redirect
        context['contentAlert'] = _('Esta seguro de registrar este pedido..!')
        context['titleAlert'] = _('Registrar nuevo Pedido')
        context['formProducto'] = ProductoForm()
        return context