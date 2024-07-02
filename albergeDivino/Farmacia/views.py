from django.shortcuts import render


def paginaPrincipal(request):
    return render(request, 'servicioMedico/principal.html')

def altaMedicamentos(request):
    return render(request, 'servicioMedico/altaMedicamentos.html')

def salidaMedicamentos(request):
     return render(request, 'servicioMedico/salidaMedicamentos.html')

def verMedicamentos(request):
     return render(request, 'servicioMedico/verMedicamentos.html')