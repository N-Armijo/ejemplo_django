from django.shortcuts import render
from django.http import HttpResponse 
from agregar_listar_tarea.views import lista_tareas

# Create your views here.
# lista_tareas = []
def resumen(request):
    global lista_tareas
    total_tareas = len(lista_tareas)
    html_content = f'''
        <!DOCTYPE html>
        <html lang="es-CL">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Resumen</title>
            </head>
            <body>
                <h1>Resumen</h1>
                <h2>Total de Tareas</h2>
                <p>Total : {total_tareas}</p>
                <a href="/">Volver</a>
            </body>
        </html>
    '''
    return HttpResponse(html_content)