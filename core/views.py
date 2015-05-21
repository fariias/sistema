from django.shortcuts import render
from forms import ClienteForm, ContratoForm, RastreadorForm
from models import Cliente, Contrato, Rastreador
from django.shortcuts import redirect
def home(request):
    clientes = Cliente.objects.all()
    return render(request, 'base.html')
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})
def ccliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientes')
    else:
        form = ClienteForm()
    return render(request, 'paginas/ccliente.html', {'form': form})
def contratos(request):
    contratos = Contrato.objects.all()
    return render(request, 'paginas/contratos.html', {'contratos': contratos})
def ccontrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/contratos')
    else:
        form = ContratoForm()
    return render(request, 'paginas/ccontrato.html', {'form': form})
def rastreadores(request):
    rastreadores = Rastreador.objects.all()
    return render(request, 'paginas/rastreadores.html', {'rastreadores': rastreadores})
def crastreador(request):
    if request.method == 'POST':
        form = RastreadorForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/rastreadores')
    else:
        form = RastreadorForm()
    return render(request, 'paginas/crastreador.html', {'form': form})
def contrato(request,id):
    contrato = Contrato.objects.get(id=id)
    cliente = Cliente.objects.get(nome=contrato.cliente)
    return render(request, 'contrato.html',{'contrato':contrato,'cliente':cliente})