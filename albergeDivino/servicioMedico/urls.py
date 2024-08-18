"""
URL configuration for servicioMedico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from farmacia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.paginaPrincipal, name="PaginaPrincipal"),
    path("altaMedicamento/", views.altaMedicamentos, name="altaMedicamentos"),
    path("salidaMedicamento/", views.salidaMedicamentos, name="salidaMedicamentos"),
    path("verMedicamento/", views.verMedicamentos, name="verMedicamentos"),
    path('alta/',views.alta,name="alta"),
    path('salidaMedicamentos/', views.salidaMedicamentos, name='salida_medicamentos'),
    path('salida/',views.salida, name='salida'),
    path('editar/<int:medicamento_id>/', views.editarMedicamento, name='editar_medicamento'),
    path('eliminar/<int:medicamento_id>/', views.eliminarMedicamento, name='eliminar_medicamento'),
    path("medicamentosAsigados/", views.medicamentosAsignados, name="medicamentosAsigados"),

]
