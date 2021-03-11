from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


# Create your views here.

class LoginFormView(LoginView):
    template_name = 'user/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Iniciar Sesion'
        return context

