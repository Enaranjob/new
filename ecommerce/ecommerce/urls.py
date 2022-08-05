"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from ventas.views import inicio,articulo,cliente,crearCliente,venta,prestamos,lisempleados,nuevoPrestamo,editarPrestamo,lisPrestamos,detallePrestamo,infoPrestamos
from django.conf.urls.static import static
from ecommerce import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('articulo/', articulo, name='articulo'),
    path('cliente/', cliente, name='cliente'),
    path('crearcliente/', crearCliente, name='crearcliente'),
    path('venta/', venta, name='venta'),
    path('prestamos/', prestamos, name='prestamos'),
    path('lisempleados/', lisempleados, name='lisempleados'),
    path('nuevoprestamo/', nuevoPrestamo, name='nuevoprestamo'),
    path('lisprestamos/', lisPrestamos, name='lisprestamos'),
    path('detalleprestamo/', detallePrestamo, name='detalleprestamo'),
    path('editarprestamo/', editarPrestamo, name='editarprestamo'),
    path('infoprestamos/', infoPrestamos, name='infoprestamos'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)