from django.shortcuts import render, get_object_or_404, redirect
from .models import Utenza, Cliente, Fattura
from .forms import UtenzaForm

def utenze_list(request):
    qs = Utenza.objects.select_related('cliente').all()
    stato = request.GET.get('stato')
    citta = request.GET.get('citta')
    cliente = request.GET.get('cliente')

    if stato:
        qs = qs.filter(stato=stato)
    if citta:
        qs = qs.filter(citta__icontains=citta)
    if cliente:
        qs = qs.filter(cliente__id=cliente)

    clienti = Cliente.objects.all()
    return render(request, 'una_acies/utenze_list.html', {
        'utenze': qs, 'clienti': clienti,
        'filtro_stato': stato, 'filtro_citta': citta, 'filtro_cliente': cliente
    })

def utenza_create(request):
    if request.method == 'POST':
        form = UtenzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('utenze_list')
    else:
        form = UtenzaForm()
    return render(request, 'una_acies/utenze_form.html', {'form': form})

def utenza_update(request, pk):
    utenza = get_object_or_404(Utenza, pk=pk)
    if request.method == 'POST':
        form = UtenzaForm(request.POST, instance=utenza)
        if form.is_valid():
            form.save()
            return redirect('utenze_list')
    else:
        form = UtenzaForm(instance=utenza)
    return render(request, 'una_acies/utenze_form.html', {'form': form})

def utenza_delete(request, pk):
    utenza = get_object_or_404(Utenza, pk=pk)
    if request.method == 'POST':
        utenza.delete()
        return redirect('utenze_list')
    return render(request, 'una_acies/utenze_confirm_delete.html', {'utenza': utenza})

def clienti_list(request):
    qs = Cliente.objects.all()
    città = request.GET.get('citta')
    ragione = request.GET.get('ragione')
    if città:
        qs = qs.filter(citta__icontains=città)
    if ragione:
        qs = qs.filter(ragione_sociale__icontains=ragione)
    return render(request, 'una_acies/clienti_list.html', {
        'clienti': qs, 'filtro_citta': città, 'filtro_ragione': ragione
    })

def fatture_list(request):
    qs = Fattura.objects.all()
    data_da = request.GET.get('data_da')
    data_a = request.GET.get('data_a')
    if data_da:
        qs = qs.filter(data__gte=data_da)
    if data_a:
        qs = qs.filter(data__lte=data_a)
    return render(request, 'una_acies/fatture_list.html', {
        'fatture': qs, 'filtro_da': data_da, 'filtro_a': data_a
    })
