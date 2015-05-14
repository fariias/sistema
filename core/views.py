from django.shortcuts import render
from forms import ClienteForm,ContratoForm,RastreadorForm
from models import Cliente,Contrato,Rastreador
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
    return render(request, 'paginas/contratos.html',{'contratos':contratos})
def ccontrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = ContratoForm()
    return render(request, 'paginas/ccontrato.html',{'form':form})
def rastreadores(request):
    rastreadores = Rastreador.objects.all()
    return render(request, 'paginas/rastreadores.html',{'rastreadores':rastreadores})
def crastreador(request):
    if request.method == 'POST':
        form = RastreadorForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = RastreadorForm()
    return render(request, 'paginas/crastreador.html',{'form':form})