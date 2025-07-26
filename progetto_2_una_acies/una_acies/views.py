from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Cliente, Utenza, Fattura, Lettura
from .forms import UtenzaForm, LetturaForm
from django.db.models import Q

def index(request):
    return redirect('utenze_list')

# Views per i clienti - solo visualizzazione
def clienti_list(request):
    filtro_citta = request.GET.get('citta', '')
    filtro_ragione = request.GET.get('ragione', '')
    
    clienti_query = Cliente.objects.all()
    
    if filtro_citta:
        clienti_query = clienti_query.filter(citta__icontains=filtro_citta)
    if filtro_ragione:
        clienti_query = clienti_query.filter(ragione_sociale__icontains=filtro_ragione)
    
    paginator = Paginator(clienti_query.order_by('ragione_sociale'), 10)
    page_number = request.GET.get('page', 1)
    clienti = paginator.get_page(page_number)
    
    context = {
        'clienti': clienti,
        'filtro_citta': filtro_citta,
        'filtro_ragione': filtro_ragione
    }
    
    return render(request, 'una_acies/clienti_list.html', context)

# Views per le utenze - CRUD completo
def utenze_list(request):
    filtro_cliente = request.GET.get('cliente', '')
    filtro_citta = request.GET.get('citta', '')
    filtro_stato = request.GET.get('stato', '')
    filtro_da = request.GET.get('data_da', '')
    filtro_a = request.GET.get('data_a', '')
    
    utenze_query = Utenza.objects.all()
    
    if filtro_cliente:
        utenze_query = utenze_query.filter(
            Q(cliente__ragione_sociale__icontains=filtro_cliente) | 
            Q(cliente__codice_fiscale__icontains=filtro_cliente)
        )
    if filtro_citta:
        utenze_query = utenze_query.filter(citta__icontains=filtro_citta)
    if filtro_stato:
        utenze_query = utenze_query.filter(stato=filtro_stato)
    if filtro_da:
        utenze_query = utenze_query.filter(data_apertura__gte=filtro_da)
    if filtro_a:
        utenze_query = utenze_query.filter(data_apertura__lte=filtro_a)
    
    paginator = Paginator(utenze_query.order_by('-data_apertura'), 10)
    page_number = request.GET.get('page', 1)
    utenze = paginator.get_page(page_number)
    
    context = {
        'utenze': utenze,
        'filtro_cliente': filtro_cliente,
        'filtro_citta': filtro_citta,
        'filtro_stato': filtro_stato,
        'filtro_da': filtro_da,
        'filtro_a': filtro_a
    }
    
    return render(request, 'una_acies/utenze_list.html', context)

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
    if Lettura.objects.filter(utenza=utenza).exists():
        return render(request, 'una_acies/utenze_delete_blocked.html', {'utenza': utenza})
    if request.method == 'POST':
        utenza.delete()
        return redirect('utenze_list')
    return render(request, 'una_acies/utenze_confirm_delete.html', {'utenza': utenza})

def utenza_letture(request, pk):
    utenza = get_object_or_404(Utenza, pk=pk)
    letture = Lettura.objects.filter(utenza=utenza).order_by('-data')
    paginator = Paginator(letture, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'una_acies/utenza_letture.html', {
        'utenza': utenza, 'letture': page_obj
    })

# Views per le fatture - solo visualizzazione
def fatture_list(request):
    filtro_da = request.GET.get('data_da', '')
    filtro_a = request.GET.get('data_a', '')
    min_totale = request.GET.get('min_totale', '')
    max_totale = request.GET.get('max_totale', '')
    
    fatture_query = Fattura.objects.all()
    
    if filtro_da:
        fatture_query = fatture_query.filter(data__gte=filtro_da)
    if filtro_a:
        fatture_query = fatture_query.filter(data__lte=filtro_a)
    if min_totale:
        fatture_query = fatture_query.filter(totale__gte=min_totale)
    if max_totale:
        fatture_query = fatture_query.filter(totale__lte=max_totale)
    
    paginator = Paginator(fatture_query.order_by('-data'), 10)
    page_number = request.GET.get('page', 1)
    fatture = paginator.get_page(page_number)
    
    context = {
        'fatture': fatture,
        'filtro_da': filtro_da,
        'filtro_a': filtro_a,
        'min_totale': min_totale,
        'max_totale': max_totale
    }
    
    return render(request, 'una_acies/fatture_list.html', context)

def fattura_letture(request, pk):
    fattura = get_object_or_404(Fattura, pk=pk)
    letture = Lettura.objects.filter(fattura=fattura).order_by('-data')
    return render(request, 'una_acies/fattura_letture.html', {
        'fattura': fattura, 'letture': letture
    })

# View per la creazione di letture (solo dall'utenza)
def lettura_create(request):
    utenza_id = request.GET.get('utenza')
    if not utenza_id:
        return redirect('utenze_list')
        
    utenza = get_object_or_404(Utenza, pk=utenza_id)
    
    if request.method == 'POST':
        form = LetturaForm(request.POST)
        if form.is_valid():
            lettura = form.save()
            return redirect('utenza_letture', pk=utenza.pk)
    else:
        form = LetturaForm(initial={'utenza': utenza})
    
    return render(request, 'una_acies/lettura_form.html', {'form': form, 'utenza': utenza})