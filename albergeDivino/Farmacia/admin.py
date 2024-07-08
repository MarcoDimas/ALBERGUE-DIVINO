from django.contrib import admin

from .models import Medicamento, AsignacionSuministro

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('categoria', 'nombre', 'clave', 'descripcion', 'fecha_caducidad', 'cantidad', 'status')
    search_fields = ('categoria', 'nombre', 'clave', 'descripcion', 'fecha_caducidad', 'cantidad', 'status')
    date_hierarchy = 'created'
    list_filter = ('categoria', 'nombre')


class AdministrarAsignacionSuministro(admin.ModelAdmin):
    list_display = ('asignado_a', 'medicamento', 'fecha_asignacion', 'cantidad')
    search_fields = ('asignado_a', 'medicamento__nombre', 'fecha_asignacion')
    date_hierarchy = 'fecha_asignacion'
    list_filter = ('asignado_a', 'medicamento__nombre', 'fecha_asignacion')

admin.site.register(Medicamento, AdministrarModelo)
admin.site.register(AsignacionSuministro, AdministrarAsignacionSuministro)