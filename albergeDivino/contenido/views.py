from django.shortcuts import render


def paginaPrincipal(request):
    return render(request, 'servicioMedico/principal.html')

def Cursos(request):
    return render(request, 'servicioMedico/cursos.html')

def contacto(request):
     return render(request, 'servicioMedico/contacto.html')