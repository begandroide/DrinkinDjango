from django.contrib import admin

from .models import Tramites 
# Register your models here.


admin.AdminSite.site_header = "Ubacán Administración"
admin.AdminSite.site_title = "Ubacán | UTFSM"

class TramitesAdmin(admin.ModelAdmin):
                    list_display = ('nombre_tarea', 'descripcion_tarea')

admin.site.register(Tramites,TramitesAdmin)
