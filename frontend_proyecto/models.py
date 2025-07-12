from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=50) # Aumentado por si acaso
    # MEJORA: ImageField es el campo correcto para subir imágenes.
    # 'upload_to' especifica la subcarpeta dentro de MEDIA_ROOT donde se guardarán.
    subir_imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)

    def __str__(self):
        return self.titulo