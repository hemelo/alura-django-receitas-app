from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'autor', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria', 'publicada' )
    list_editable = ('publicada',)
    list_per_page = 10

# Register your models here.
admin.site.register(Receita, ListandoReceitas)