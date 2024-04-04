from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
def listar_receitas(request):
    nome = 'Eduardo'
    ingredientes = ['Farinha', 'Ovo', 'Manteiga', 'Leite']
    # dicionario que vai levar os dados para o template
    # chave : valor
    context = {
        'Endereco' : 'Av. Marechal tito',
        'Bairro' : 'São Miguel Paulista', 
        'Cidade' : 'São Paulo',
        'Estado' : 'SP',
        'Nome' : nome,
        'Ingredientes' : ingredientes

    }
    # qual template essa view ira retornar
    return render(request, 'receitas.html', context)
