from django.contrib import admin
from .models import Proyecto # Importamos el modelo Proyecto

# Registramos el modelo para que aparezca en el sitio de administración.
# admin.ModelAdmin.list_display = ('titulo', 'tecnologia') # Opcional: para mostrar más columnas
admin.site.register(Proyecto)
