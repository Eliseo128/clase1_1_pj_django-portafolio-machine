from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Cuando alguien visite la raíz del sitio, se dirigirán a las URLs
    # definidas en 'frontend_proyecto.urls'
    path('', include('frontend_proyecto.urls')),
]

# Esto es necesario para que el servidor de desarrollo sirva los archivos de medios (imágenes)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)