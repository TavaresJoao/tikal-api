from django.contrib import admin
from .models import *


class ListTelefone(admin.ModelAdmin):
    list_display = ('id', 'ddd', 'numero', 'tipo')
    list_display_links = ('id',)
    list_per_page = 10

class ListEmail(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('id', 'email',)
    list_per_page = 10

class ListCliente(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nasc', 'sexo', 'telefone', 'email')
    list_display_links = ('id', 'rg', 'cpf',)
    list_per_page = 10

admin.site.register(Telefone, ListTelefone)
admin.site.register(Email, ListEmail)
admin.site.register(Cliente, ListCliente)
