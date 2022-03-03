from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from receitas_app.models import Receita 
from .forms import CadastroForm, LoginFromEmailForm

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username'), email=form.cleaned_data['email'], password=form.cleaned_data['password'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'] )
            user.save()
            return redirect('login')
        else:
            data = { 'form': form }
            return render(request, "cadastro.html", data)
    
    form = CadastroForm()
    data = { 'form': form }
    return render(request, "cadastro.html", data)

def login(request):
    if request.method == 'POST':
        form = LoginFromEmailForm(request.POST)
        if form.is_valid():
            username = User.objects.filter(email=form.cleaned_data.get('email')).values_list('username', flat=True)[0]
            user = auth.authenticate(request, username=username, password=form.cleaned_data.get('password'))

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                form.add_error('password', 'Senha inválida')
                data = { 'form': form }
                return render(request, "login.html", data)
        else:
            data = { 'form': form }
            return render(request, "login.html", data)
    
    form = LoginFromEmailForm()
    data = { 'form': form }
    return render(request, "login.html", data)



def dashboard(request):
    if not request.user.is_authenticated:
        redirect('index')

    id = request.user.id
    receitas = Receita.objects.order_by('-data_receita').filter(autor=id)
    data = { 'receitas': receitas }
    return render(request, 'dashboard.html', data)

def logout(request):
    auth.logout(request)
    return redirect('index')