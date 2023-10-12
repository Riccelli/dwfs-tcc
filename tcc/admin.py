from django.contrib import admin
from .models import Indice, Modalidade, Programa, Cliente, Proposta, Telefone, Aliquota
from import_export.admin import ExportActionModelAdmin


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1


class ClienteAdmin(ExportActionModelAdmin):
    inlines = [TelefoneInline]


class AliquotaInline(admin.TabularInline):
    model = Aliquota
    extra = 1


class IndiceAdmin(ExportActionModelAdmin):
    inlines = [AliquotaInline]


class ModalidadeAdmin(ExportActionModelAdmin):
    pass


class ProgramaAdmin(ExportActionModelAdmin):
    pass


class PropostaAdmin(ExportActionModelAdmin):
    pass


admin.site.register(Indice, IndiceAdmin)
admin.site.register(Modalidade, ModalidadeAdmin)
admin.site.register(Programa, ProgramaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proposta, PropostaAdmin)
