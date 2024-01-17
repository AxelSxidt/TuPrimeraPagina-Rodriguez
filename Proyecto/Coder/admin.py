from django.contrib import admin
from . import models

admin.site.register(models.Podologo)
admin.site.register(models.Cita)
admin.site.register(models.Paciente)
admin.site.register(models.Tratamiento)
admin.site.register(models.TratamientoParaCita)
