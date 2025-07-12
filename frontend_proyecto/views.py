from django.shortcuts import render, get_object_or_404
from .models import Proyecto

def ver_proyectos(request):
    """
    Esta vista obtiene todos los proyectos de la base de datos
    y los pasa al template 'ver_proyectos.html'.
    """
    proyectos = Proyecto.objects.all()
    context = {
        'proyectos': proyectos
    }
    return render(request, 'frontend_proyecto/ver_proyectos.html', context)

def detalles_proyecto(request, proyecto_id):
    """
    Esta vista obtiene un proyecto específico por su ID.
    Si el proyecto no existe, muestra una página de error 404.
    """
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    context = {
        'proyecto': proyecto
    }
    return render(request, 'frontend_proyecto/detalles_proyecto.html', context)