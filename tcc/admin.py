from django.contrib import admin
from .models import Indice, Modalidade, Programa, Cliente, Proposta, Telefone, Aliquota


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1


class ClienteAdmin(admin.ModelAdmin):
    inlines = [TelefoneInline]


class AliquotaInline(admin.TabularInline):
    model = Aliquota
    extra = 1


class IndiceAdmin(admin.ModelAdmin):
    inlines = [AliquotaInline]


admin.site.register(Indice, IndiceAdmin)
admin.site.register(Modalidade)
admin.site.register(Programa)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proposta)
