from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .forms import ReceitaForm
from .models import Receita

# Create your views here.

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    paginator = Paginator(receitas, 12)
    page = request.GET.get('page')
    receitas_per_page = paginator.get_page(page)
    
    if 'search' in request.GET:
        search = request.GET['search']
        receitas = receitas.filter(nome__icontains=search).filter(publicada=True)
        data = { 'receitas': receitas }
        return render(request, 'index.html', data)

    data = { 'receitas': receitas_per_page }
    return render(request, 'index.html', data)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id, publicada=True)
    data = { 'receita': receita }
    return render(request, 'data.html', data)

def nova_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST, request.FILES)
        form.fields['foto_receita'].required = True

        if form.is_valid():
            user = get_object_or_404(User, pk=request.user.id)
            receita = Receita.objects.create(
                autor=user, 
                nome=form.cleaned_data.get('nome'),
                ingredientes=form.cleaned_data.get('ingredientes'),
                modo_preparo=form.cleaned_data.get('modo_preparo'),
                tempo_preparo=form.cleaned_data.get('tempo_preparo'),
                rendimento=form.cleaned_data.get('rendimento'),
                categoria=form.cleaned_data.get('categoria'),
                foto_receita=form.cleaned_data.get('foto_receita'),
                )
            receita.save()

            return redirect('dashboard')
        else:
            data = { 'form': form }
            return render(request, "cria_receita.html", data)

    form = ReceitaForm()
    data = { 'form': form }
    return render(request, "cria_receita.html", data)

def deleta_receita(request, receita_id):
    if request.method == 'POST':
        receita = get_object_or_404(Receita, pk=receita_id, autor=request.user.id)
        receita.delete()

    return redirect('dashboard')

def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id, autor=request.user.id)

    if request.method == 'GET':
        form = ReceitaForm(initial={ 'nome': receita.nome, 'ingredientes': receita.ingredientes, 'modo_preparo': receita.modo_preparo, 'tempo_preparo': receita.tempo_preparo, 'rendimento': receita.rendimento, 'categoria': receita.categoria })
        data = { 'form': form, 'receita_id': receita.id }
        return render(request, "edita_receita.html", data)
    else: 
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            receita.nome = form.cleaned_data.get('nome')
            receita.ingredientes = form.cleaned_data.get('ingredientes')
            receita.modo_preparo = form.cleaned_data.get('modo_preparo')
            receita.tempo_preparo = form.cleaned_data.get('tempo_preparo')
            receita.rendimento = form.cleaned_data.get('rendimento')
            receita.categoria = form.cleaned_data.get('categoria')

            if 'foto_receita' in request.FILES:
                receita.foto_receita = form.cleaned_data.get('foto_receita')

            receita.save()
        else:
            data = { 'form': form, 'receita_id': receita.id }
            return render(request, "edita_receita.html", data)

    return redirect('dashboard')