from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export.admin import ExportActionModelAdmin
from .models import Indice, Modalidade, Programa, Cliente, Proposta, Parcela, Telefone, Aliquota


class ClienteInline(admin.StackedInline):
    model = Cliente
    can_delete = False


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ClienteInline]


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


class ParcelaInline(admin.TabularInline):
    model = Parcela
    extra = 0


class PropostaAdmin(ExportActionModelAdmin):
    inlines = [ParcelaInline]


admin.site.register(Indice, IndiceAdmin)
admin.site.register(Modalidade, ModalidadeAdmin)
admin.site.register(Programa, ProgramaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proposta, PropostaAdmin)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
