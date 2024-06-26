from django.contrib import admin

from .models import Medicamento

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('categoria', 'nombre', 'clave', 'descripcion', 'fecha_caducidad', 'cantidad', 'status')
    search_fields = ('categoria', 'nombre', 'clave', 'descripcion', 'fecha_caducidad', 'cantidad', 'status')
    date_hierarchy = 'created'
    list_filter = ('categoria', 'nombre')


admin.site.register(Medicamento, AdministrarModelo)