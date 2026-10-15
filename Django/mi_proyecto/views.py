import random
import random  # 1. Importar la librería para elegir al azar
from django.shortcuts import render
from .artes import lista_de_artes, lista_de_artes_gif  # 1.1


def inicio(request):
    return render(
        request,
        'inicio.html',
    )


def arte_aleatorio_gif(request):
    print("--- ENTRANDO A ARTE GIF ---")
    modo = request.GET.get('modo', 'oscuro')
    indice_actual = request.session.get('indice_arte', 0)

    # Asegúrate de que lista_de_artes_gif esté definida en tu archivo artes.py
    # y que lo hayas importado correctamente arriba con:
    # from .artes import lista_de_artes, lista_de_artes_gif

    arte_elegido = lista_de_artes_gif[indice_actual % len(lista_de_artes_gif)]
    request.session['indice_arte'] = indice_actual + 1
    print("Longitud de la lista:", len(lista_de_artes_gif))
    # Esto imprimirá la longitud en tu consola donde corre el servidor (terminal)

    return render(request, 'arte.html', {
        'dibujo': arte_elegido,
        # <--- Este nombre debe ser igual al que usas en el HTML
        'lista_artes_gif': lista_de_artes_gif,
        'modo': modo
    })


def arte_aleatorio(request):
    print("--- ENTRANDO A ARTE ALEATORIO ---")
    modo = request.GET.get('modo', 'original')

    # 1. Obtenemos el historial de la sesión (o una lista vacía si es nuevo)
    ultimo_arte = request.session.get('ultimo_arte')

    # 2. Creamos una lista filtrada que NO contenga el último arte mostrado
    # (Si la lista es muy pequeña, evitamos que se quede vacía)
    opciones = [arte for arte in lista_de_artes if arte != ultimo_arte]

    # Si por alguna razón no quedan opciones (ej. solo hay 1 arte), usamos la lista completa
    if not opciones:
        opciones = lista_de_artes

    # 3. Elegimos al azar de las opciones disponibles
    arte_elegido = random.choice(opciones)

    # 4. Guardamos el elegido en la sesión para la próxima vez
    request.session['ultimo_arte'] = arte_elegido

    return render(request, 'arte.html', {
        'dibujo': arte_elegido,
        'modo': modo
    })

    # 4. Se lo mandamos a tu plantilla HTML


# def arte_aleatorio(request):

#     modo = request.GET.get('modo', 'original')

#     # 3. Le decimos a Python que elija uno al azar de esa lista
#     arte_elegido = random.choice(lista_de_artes)

#     return render(request, 'arte.html', {
#         'dibujo': arte_elegido,
#         'modo': modo  # <-- Pasamos el estado a la plantilla
#     })
