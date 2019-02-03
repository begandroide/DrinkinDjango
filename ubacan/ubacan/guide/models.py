from django.db import models

# Create your models here.

class Tramites(models.Model):
                    nombre_tarea = models.CharField(max_length = 50)
                    descripcion_tarea = models.CharField(max_length = 250)
                    pub_date = models.DateTimeField('Date Published')
                    
                    def __str__(self):
                                        return self.nombre_tarea

