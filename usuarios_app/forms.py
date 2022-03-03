from django import forms
from django.contrib.auth.models import User


class CadastroForm(forms.Form):
    first_name = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder': 'Ex.:Guilherme', 'class': 'form-control'}), required=True)
    last_name = forms.CharField(label="Sobrenome", widget=forms.TextInput(attrs={'placeholder': 'Ex.:Lima', 'class': 'form-control'}), required=True)
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'placeholder': 'guilherme02313219', 'class': 'form-control'}), required=True)
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Ex.: guilherme@receitas.com', 'class': 'form-control'}), required=True)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'}), required=True)
    passwordConfirm = forms.CharField(label="Confirmar senha", widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha mais uma vez', 'class': 'form-control'}), required=True)

    def clean_first_name(self):
        first = self.cleaned_data.get('first_name')
        if any(char.isdigit() for char in first):
            raise forms.ValidationError("Não inclua números no nome.")

        if ' ' in first:
            raise forms.ValidationError("Não inclua espaços no nome.")

        return first

    def clean_last_name(self):
        last = self.cleaned_data.get('last_name')
        if any(char.isdigit() for char in last):
            raise forms.ValidationError("Não inclua números no nome.")

        if ' ' in last:
            raise forms.ValidationError("Não inclua espaços no nome.")

        return last

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username já cadastrado.");

        if ' ' in username:
            raise forms.ValidationError("Não inclua espaços no username.")

        return username

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        pwd2 = self.cleaned_data.get('passwordConfirm')

        if pwd is pwd2:
            raise forms.ValidationError("As senhas não se confirmam.");

        return pwd

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email já cadastrado.");

        return email

class LoginFromEmailForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Digite seu email', 'class': 'form-control'}), required=True)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'}), required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email não encontrado");

        return email

    def clean_password(self):
        pwd = self.cleaned_data.get('password')

        if pwd == "":
            raise forms.ValidationError("A senha está vazia");

        return pwd

class NovaReceita(forms.Form):
    nome = forms.CharField(label="Nome receita", widget=forms.TextInput(attrs={'placeholder': 'Ex. Suco de limão', 'class': 'form-control'}), required=True)

    ingredientes = forms.CharField(min_length=20, label="Ingredientes", widget=forms.Textarea(attrs={'placeholder': 'Ex. 2 Limões; 200ml de água', 'class': 'form-control', 'cols':'30', 'rows':'10'}), required=True)

    modo_preparo = forms.CharField(min_length=100, label="Modo de preparo", widget=forms.Textarea(attrs={'placeholder': 'Ex. Corte o limão com cuidado e exprema no copo; Misture com a água e sirva.', 'class': 'form-control', 'cols':'30', 'rows':'10'}), required=True)

    tempo_preparo = forms.CharField(label="Tempo de preparo (minutos)", widget=forms.NumberInput(attrs={'placeholder': 'Ex. 2', 'class': 'form-control'}), required=True)

    rendimento = forms.CharField(label="Rendimento", widget=forms.TextInput(attrs={'placeholder': 'Ex. Serve 1 pessoa', 'class': 'form-control'}), required=True)

    categoria = forms.CharField(label="Categoria", widget=forms.TextInput(attrs={'placeholder': 'Ex. Sobremesa', 'class': 'form-control'}), required=True)

    foto_receita = forms.ImageField(label="Foto", widget=forms.FileInput(attrs={'class': 'form-control'}), required=True)