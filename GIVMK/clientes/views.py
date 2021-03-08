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
from .models import Client
from .forms import ClienteForm

# Create your views here.

class CustomerListView(ListView):

    model = Client
    template_name = 'clientes/customersList.html'

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
                for i in Client.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = _('Listado de Clientes')
        return context

class ClientCreateView(CreateView):
    # permission_required = ['escuela.view_escuela', 'escuela.add_escuela']
    model = Client
    form_class = ClienteForm
    # fields = '__all__'
    success_url = reverse_lazy('customersList')
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
        context['titulo'] = _('Registrar un Nuevo Cliente')
        context['lazyUrl'] = self.url_redirect
        context['contentAlert'] = _('Esta seguro de crerar este nuevo cliente')
        context['titleAlert'] = _('Crear nuevo Cliente')
        return context

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('customersList')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClienteForm
    template_name = 'clientes/client_form.html'
    success_url = reverse_lazy('customersList')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                cli = Client.objects.filter(id=kwargs['pk']).get()
                cli.firts_name = request.POST['firts_name']
                cli.last_name = request.POST['last_name']
                cli.gender = request.POST['gender']
                cli.idNumber = request.POST['idNumber']
                cli.nacimiento = request.POST['nacimiento']
                cli.NIT = request.POST['NIT']
                cli.tel = request.POST['tel']
                # Validamos si trae cambio de img
                if request.FILES:
                    print('Si trae imagen')
                    cli.img = request.FILES['img']
                cli.save()
                print(cli.img)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        context['titulo'] = _('Editar Cliente')
        context['lazyUrl'] = self.url_redirect
        context['contentAlert'] = _('Esta seguro de editar el cliente')
        context['titleAlert'] = _('Editar Cliente')
        return context

class ClientDetailView(DetailView):
    model = Client