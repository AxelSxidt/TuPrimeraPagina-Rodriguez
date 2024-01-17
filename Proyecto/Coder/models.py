from django.db import models

class Podologo(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    mail = models.EmailField()

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    nombre = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, blank=True)
    hora = models.DateTimeField()
    podologo = models.ForeignKey(Podologo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}-{self.hora.strftime('%H:%M')}"


class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.nombre} ${self.costo}" 

class TratamientoParaCita(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.cita}:{self.tratamiento}"
