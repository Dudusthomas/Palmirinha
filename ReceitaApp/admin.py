from django.contrib import admin
from ReceitaApp.models import Categoria, Receita

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    list_display_links = ["nome"]
    list_filter = ["nome"]

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ingredientes', 'modo_de_preparo', 'grau_de_dificuldade']
    list_display_links = ['nome']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)



# Register your models here.
