from django.shortcuts import HttpResponse
from django.shortcuts import render
html_base = """
 <h1>Shopping Car</h1>
 <ul>
   <li><a href="/">Inicio</a></li>
   <li><a href="/articulo/">Articulos</a></li>
   <li><a href="/cliente/">Clientes</a></li>
   <li><a href="/venta/">Ventas</a></li>
   <li><a href="/consulta/">Consultas</a></li>
 </li>
"""
def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)


def articulo(request):
  return HttpResponse(html_base+
    """<h2>Mantenimiento de Articulo</h2>
       <p>List de articulos</p>""")

def cliente(request):
  data = {
      'titulo':'GESTION DE CLIENTES',
      'crear_url': '/crearcliente',
      'listar_url': '/cliente',
      'cancelar_url':'/venta',
  }
  return render(request, "ventas/clientes/listCliente.html",data)

def crearCliente(request):
  data = {
      'titulo':'MANTENIMIENTO DE CLIENTES',
      'crear_url':'/crearcliente',
      'action':'add',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/formCliente.html",data)

def venta(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "ventas/ventas.html",data)

def prestamos(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "prestamos/prestamos.html",data)

def lisempleados(request):
  data = {
      'titulo': 'GESTION EMPLEADOS',
      'crear_url': '/lisempleados',
      'listar_url': '/prestamos',
  }
  return render(request, "prestamos/empleados/lisempleados.html",data)

def nuevoPrestamo(request):
  data = {
      'titulo':'INGRESAR PRESTAMO',
      'crear_url': '/lisprestamos',
      'action': 'add',
      'listar_url': '/lisprestamos',
  }
  return render(request, "prestamos/empleados/nuevoprestamo.html",data)

def editarPrestamo(request):
  data = {
    'titulo':'EDITAR PRESTAMO',
    'crear_url': '/lisprestamos',
    'action': 'add',
    'listar_url': '/lisprestamos',
}
  return render(request, "prestamos/empleados/editarprestamo.html",data)

def lisPrestamos(request):
  data = {
      'titulo':'LISTA DE PRESTAMOS',
      'crear_url': '/nuevoprestamo',
      'action': 'add',
      'listar_url': '/lisprestamos',
      'cancelar_url':'/prestamos',
  }
  return render(request, "prestamos/empleados/lisprestamos.html",data)

def detallePrestamo(request):
  data = {
    'crear_url': '/detalleprestamo',
    'titulo':'DETALLE DEL PRESTAMO',
    'listar_url': '/prestamos',
  }
  return render(request, "prestamos/empleados/detalleprestamo.html",data)

def infoPrestamos(request):
  data = {
    'crear_url': '/infoprestamos',
    'titulo':'DETALLE DEL PRESTAMO',
    'listar_url': '/detalleprestamo',
  }
  return render(request, "prestamos/empleados/infoprestamos.html",data)