from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .models import Producto
from .forms import ProductoForm

# Create your views here.

class ProductosListView(ListView):

    model = Producto
    template_name = 'catalogo/producto_list.html'

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
                for i in Producto.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Listado de Productos')
        return context

class ProductoCreateView(CreateView):
    # permission_required = ['escuela.view_escuela', 'escuela.add_escuela']
    model = Producto
    form_class = ProductoForm
    # fields = '__all__'
    success_url = reverse_lazy('productosList')
    url_redirect = success_url

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Sobreescribimos el metodo POST
    def post(self, request, *args, **kwargs):
        data = {}
        # Campturamos el error
        try:
            # Verificamos que la accion que trae el request agregar
            action = request.POST['action']
            if action == 'add':
                # Obtenemos nuestro formulario
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a Ninguna Opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'add'
        context['titulo'] = _('Registrar un Nuevo Producto')
        context['lazyUrl'] = self.url_redirect
        context['contentAlert'] = _('Esta seguro de crerar este nuevo producto')
        context['titleAlert'] = _('Crear nuevo Producto')
        return context

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('productosList')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'catalogo/producto_form.html'
    success_url = reverse_lazy('productosList')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                pro = Producto.objects.filter(id=kwargs['pk']).get()
                pro.nombre = request.POST['nombre']
                pro.precio_consultora = request.POST['precio_consultora']
                pro.precio_catalogo = request.POST['precio_catalogo']
                pro.descripcion = request.POST['descripcion']
                # Validamos si trae cambio de img
                if request.FILES:
                    print('Si trae imagen')
                    pro.img = request.FILES['img']
                pro.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        context['titulo'] = _('Editar Producto')
        context['lazyUrl'] = self.url_redirect
        context['contentAlert'] = _('Esta seguro de editar el producto')
        context['titleAlert'] = _('Editar Producto')
        return context

class ProductoDetailView(DetailView):
    model = Producto