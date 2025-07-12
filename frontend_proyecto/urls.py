from django.urls import path
from . import views

# Este app_name ayuda a Django a diferenciar las URLs entre aplicaciones
app_name = 'frontend_proyecto'

urlpatterns = [
    # URL para la lista de proyectos. Será la página principal de la app.
    path('', views.ver_proyectos, name='lista_proyectos'),
    
    # URL para los detalles de un proyecto. Usa un conversor de path <int:proyecto_id>
    # para capturar el ID del proyecto como un entero.
    path('proyecto/<int:proyecto_id>/', views.detalles_proyecto, name='detalles_proyecto'),
]