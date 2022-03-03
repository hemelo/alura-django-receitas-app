from django.shortcuts import get_object_or_404, render
from .models import Receita

# Create your views here.

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'search' in request.GET:
        search = request.GET['search']
        receitas = receitas.filter(nome__icontains=search)

    data = { 'receitas': receitas }
    return render(request, 'index.html', data)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id, publicada=True)
    data = { 'receita': receita }
    return render(request, 'data.html', data)