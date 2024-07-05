from django.shortcuts import render
from .models import Medicamento
from .forms import MedicamentoForm
def paginaPrincipal(request):
    return render(request, 'Farmacia/principal.html')



def alta(request):
    if request.method == 'POST':
       form = MedicamentoForm(request.POST)
       if form.is_valid(): #Si los datos recibidos son correctos
              form.save() #inserta
              return render(request, 'Farmacia/altaMedicamentos.html')
    form = MedicamentoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'Farmacia/altaMedicamentos.html',{'form': form})
    

def altaMedicamentos(request):
     return render(request,"Farmacia/altaMedicamentos.html")
#Indicamos el lugar donde se renderizará el resultado
  
    

def salidaMedicamentos(request):
     return render(request, 'Farmacia/salidaMedicamentos.html')

def verMedicamentos(request):
    medicamento =Medicamento.objects.all()
    return render(request, "Farmacia/verMedicamentos.html", {'MD':medicamento})
