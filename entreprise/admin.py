from django.contrib import admin
from entreprise.models import Livre, Problematique, Postuler


class LivreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titre",)}


admin.site.register(Problematique)
admin.site.register(Postuler)
admin.site.register(Livre, LivreAdmin)
