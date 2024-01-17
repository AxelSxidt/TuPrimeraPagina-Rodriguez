from django import forms
from . import models


class PodolodoForm(forms.ModelForm):
    class Meta:
        model = models.Podologo
        fields = "__all__"

class PacienteForm(forms.ModelForm):
    class Meta:
        model = models.Paciente
        fields = "__all__"
