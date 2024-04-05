from django.shortcuts import render
from ReceitaApp.models import Receita, Categoria
 
#create categorias
def index(request):
    categorias = Categoria.objects.all()
 
    context = {
        'categorias' : categorias
    }
 
    return render(request, 'index.html', context)
 
# Create your views here.
def listar_receitas(request):
    #buscar as receitas no banco de dados utilizando ORM do Django
    receitas = Receita.objects.all()
 
    #dicionario de dados para template
    #chave : valor
    context = {
            'receitas' : receitas
    }
    #qual tmplede essa view vai retorna
    return render (request, 'receitas.html', context)

def detalhes_receita(request, id):
    
    receita = Receita.objects.get(id = id)

    context = {
        'receita' : receita
    }

    return render (request, 'receita.html', context)