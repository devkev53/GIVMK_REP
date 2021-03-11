"""GIVMK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import HomePageView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url('', include('clientes.urls')),
    url('', include('catalogo.urls')),
    url('', include('inventario.urls')),
    url('', include('core.urls')),
    url('', include('user.urls')),
]

# Truco para poder ver ficheros multimedia con el DEBUG=TRUE
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom titles para el admin
admin.site.site_header = 'Manejo Inventario MAry Kay'
#  admin.site.index_title = 'No se que poner XD'
admin.site.site_title = 'Administrador MK'
