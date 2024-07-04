from django.shortcuts import render


def paginaPrincipal(request):
    return render(request, 'Farmacia/principal.html')

def altaMedicamentos(request):
    return render(request, 'Farmacia/altaMedicamentos.html')

def salidaMedicamentos(request):
     return render(request, 'Farmacia/salidaMedicamentos.html')

def verMedicamentos(request):
     return render(request, 'Farmacia/verMedicamentos.html')