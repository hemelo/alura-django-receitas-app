from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receita/<int:receita_id>', views.receita, name='receita'),
    path('dashboard/formulario', views.nova_receita, name='nova_receita'),
    path('deletar/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
    path('editar/<int:receita_id>', views.edita_receita, name='edita_receita'),
]
