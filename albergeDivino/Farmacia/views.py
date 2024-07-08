from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento, AsignacionSuministro
from .forms import MedicamentoForm, AsignacionSuministroForm

#VISTA DEL MENU PRINCIPAL
def paginaPrincipal(request):
    return render(request, 'Farmacia/principal.html')



#VISTA PARA EL ALTA DE UN MEDICMANETO
def alta(request):
    if request.method == 'POST':
       form = MedicamentoForm(request.POST)
       if form.is_valid(): 
              form.save() 
              return render(request, 'Farmacia/altaMedicamentos.html')
    form = MedicamentoForm()
    return render(request,'Farmacia/altaMedicamentos.html',{'form': form})
    

def altaMedicamentos(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Farmacia/altaMedicamentos.html')
    else:
        form = MedicamentoForm()
    return render(request, 'Farmacia/altaMedicamentos.html', {'form': form})
  
    
def salidaMedicamentos(request):
    if request.method == 'POST':
        form = AsignacionSuministroForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('verMedicamentos')
            except ValueError as error:
                form.add_error(None, str(error))
    else:
        form = AsignacionSuministroForm()
    
    medicamentos = Medicamento.objects.all()
    return render(request, 'Farmacia/salidaMedicamentos.html', {'form': form, 'medicamentos': medicamentos})


def salida(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, id=medicamento_id)

    if request.method == 'POST':
        form = AsignacionSuministroForm(request.POST, instance=medicamento)
        if form.is_valid():
            cantidad_salida = form.cleaned_data['cantidad']
            if medicamento.cantidad >= cantidad_salida:
                medicamento.cantidad -= cantidad_salida
                medicamento.save()
                return redirect('verMedicamentos')
            else:
                form.add_error('cantidad', 'No hay suficiente cantidad disponible.')
    else:
        form = AsignacionSuministroForm(instance=medicamento)

    return render(request, 'Farmacia/salida.html', {'form': form, 'medicamento': medicamento})



#VER TODOS LOS MEDICAMENTOS REGISTRADS
def verMedicamentos(request):
    medicamento =Medicamento.objects.all()
    return render(request, "Farmacia/verMedicamentos.html", {'MD':medicamento})

#EDITAR UN MEDICAMENTO REGISTRADO
def editarMedicamento(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, id=medicamento_id)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('verMedicamentos')
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, 'Farmacia/editarMedicamento.html', {'form': form, 'medicamento': medicamento})


#ELIMINAR UN MEDICMANETO REGISTRADO
def eliminarMedicamento(request, medicamento_id):
    medicamento = get_object_or_404(Medicamento, id=medicamento_id)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('verMedicamentos')
    return render(request, 'Farmacia/eliminarMedicamento.html', {'medicamento': medicamento})



#VER LOS MEDICAMENTOS ASIGNADOS
def medicamentosAsignados(request):
    asignado =AsignacionSuministro.objects.all()
    return render(request, "Farmacia/medicamentosAsignados.html", {'MD':asignado})
