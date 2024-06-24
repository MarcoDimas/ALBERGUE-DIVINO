from django.shortcuts import render


def paginaPrincipal(request):
    return render(request, 'cursosDjango/principal.html')

def Cursos(request):
    return render(request, 'cursosDjango/cursos.html')

def contacto(request):
     return render(request, 'cursosDjango/contacto.html')