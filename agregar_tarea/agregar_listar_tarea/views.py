from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
lista_tareas = []
def agregar(request):
    global lista_tareas
    if 'tarea' in request.GET:
        tarea = request.GET.get('tarea')
        completada = request.GET.get('completada') == 'true'
        lista_tareas.append({"tarea": tarea, "status": completada})
        return redirect('')
    
    tareas_html = '<ul>'
    for tarea in lista_tareas:
        status = 'Completada' if tarea['status'] else 'Pendiente'
        tareas_html += f'<li>{tarea['tarea']} - {status}</li>'
    tareas_html += '</ul>'

    form_html = '''

        <form action="" method="GET">
            <label for="tarea">Tarea</label>
            <input type="text" id="tarea" name="tarea" required>
            <label for="completada">Completada</label>
            <input type="checkbox" id="completada" name="completada" value="true">
            <button type="submit">Guardar</button>
        </form>
    '''

    html_content = f'''
        <!DOCTYPE html>
            <html lang="es-CL">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Agregar Tareas</title>
                </head>
                <body>
                    <h1>Lista de Tareas</h1>
                    {tareas_html}
                    <h2>Crear Tarea</h2>
                    {form_html}
                    <a href="resumen">Ver resumen</a>
                </body>
            </html>
    '''
    return HttpResponse(html_content)