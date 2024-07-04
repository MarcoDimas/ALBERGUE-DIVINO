from django.shortcuts import render
from .models import Medicamento

def paginaPrincipal(request):
    return render(request, 'Farmacia/principal.html')

def altaMedicamentos(request):
    return render(request, 'Farmacia/altaMedicamentos.html')

def salidaMedicamentos(request):
     return render(request, 'Farmacia/salidaMedicamentos.html')

def verMedicamentos(request):
    medicamento =Medicamento.objects.all()
    return render(request, "Farmacia/verMedicamentos.html", {'MD':medicamento})
