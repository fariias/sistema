from django.shortcuts import render
from forms import ClienteForm,ContratoForm
from models import Cliente,Contrato
def home(request):
    clientes = Cliente.objects.all()
    return render(request, 'index.html',{'clientes':clientes})
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html',{'clientes':clientes})
def ccliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'paginas/ccliente.html',{'form':form})
def contratos(request):
    contratos = Contrato.objects.all()
    return render(request, 'clientes.html',{'contratos':contratos})
def ccontrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = ContratoForm()
    return render(request, 'paginas/ccontrato.html',{'form':form})