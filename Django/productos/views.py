from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Producto
from productos.forms import ProductoForm
# Create your views here.

# /products


def index(request):  # todas las funciones de view reciben simpre el mismo argumento
    productos = Producto.objects.all()
    # productos= Producto.objects.filter(puntaje=5)
    # productos= Producto.objects.filter(puntaje__gt=3)#mayor que 3 greater than
    # productos= Producto.objects.filter(puntaje__lte=3)#menor que 3 less than
    # productos= Producto.objects.get(id=1)#por ia
    # productos= Producto.objects.get(pk=1)#por pk
    # print(productos)
    # return HttpResponse('¯\_(ツ)_/¯ hola mundo')
    # productos = Producto.objects.all().values()
    # return JsonResponse(list(productos), safe=False)
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)

    return render(
        request,
        'detalle.html',
        context={'producto': producto})

    # try: get_object_or_404 hace todo
    #     producto = Producto.objects.get(id=producto_id)

    #     return render(
    #         request,
    #         'detalle.html',
    #         context={'producto': producto})
    # except Producto.DoesNotExist:
    #     raise Http404()


def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )
