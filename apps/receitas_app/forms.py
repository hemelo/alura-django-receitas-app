from django import forms

class ReceitaForm(forms.Form):
    nome = forms.CharField(label="Nome receita", widget=forms.TextInput(attrs={'placeholder': 'Ex. Suco de limão', 'class': 'form-control'}), required=True)

    ingredientes = forms.CharField(min_length=20, label="Ingredientes", widget=forms.Textarea(attrs={'placeholder': 'Ex. 2 Limões; 200ml de água', 'class': 'form-control', 'cols':'30', 'rows':'10'}), required=True)

    modo_preparo = forms.CharField(min_length=100, label="Modo de preparo", widget=forms.Textarea(attrs={'placeholder': 'Ex. Corte o limão com cuidado e exprema no copo; Misture com a água e sirva.', 'class': 'form-control', 'cols':'30', 'rows':'10'}), required=True)

    tempo_preparo = forms.CharField(label="Tempo de preparo (minutos)", widget=forms.NumberInput(attrs={'placeholder': 'Ex. 2', 'class': 'form-control'}), required=True)

    rendimento = forms.CharField(label="Rendimento", widget=forms.TextInput(attrs={'placeholder': 'Ex. Serve 1 pessoa', 'class': 'form-control'}), required=True)

    categoria = forms.CharField(label="Categoria", widget=forms.TextInput(attrs={'placeholder': 'Ex. Sobremesa', 'class': 'form-control'}), required=True)

    foto_receita = forms.ImageField(label="Foto", widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)