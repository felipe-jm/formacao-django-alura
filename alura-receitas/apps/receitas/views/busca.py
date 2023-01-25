from django.shortcuts import render
from receitas.models import Receita

def busca(request):
  lista_receitas = Receita.objects.order_by('-data_receita').all()

  if 'buscar' in request.GET:
    nome_a_buscar = request.GET.get('buscar')
    lista_receitas = lista_receitas.filter(
      nome_receita__icontains=nome_a_buscar
    )

  dados = {
    'receitas': lista_receitas
  }

  return render(request, 'receitas/buscar.html', context=dados)