from django.contrib import admin
from django.http import HttpResponse
import csv
from django.core.mail import send_mail
from .models import Medicamento, AsignacionSuministro
from django.utils.html import format_html
from datetime import datetime  # <-- Añade esta línea

# Función para exportar a CSV
def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=medicamentos.csv'
    writer = csv.writer(response)
    writer.writerow(['Categoria', 'Nombre', 'Clave', 'Descripcion', 'Fecha de Caducidad', 'Cantidad', 'Status'])
    for obj in queryset:
        writer.writerow([obj.categoria, obj.nombre, obj.clave, obj.descripcion, obj.fecha_caducidad, obj.cantidad, obj.status])
    return response

export_as_csv.short_description = 'Exportar a CSV'

# Función para enviar recordatorio de caducidad
def enviar_recordatorio_de_caducidad(modeladmin, request, queryset):
    for obj in queryset:
        send_mail(
            'Recordatorio de Caducidad',
            f'El medicamento {obj.nombre} está próximo a caducar.',
            'admin@example.com',
            ['recipient@example.com'],
            fail_silently=False,
        )

enviar_recordatorio_de_caducidad.short_description = 'Enviar recordatorio de caducidad'

# Función para marcar medicamentos como revisados
def marcar_como_revisado(modeladmin, request, queryset):
    queryset.update(status='Revisado')
    modeladmin.message_user(request, "Medicamentos marcados como revisados.")

marcar_como_revisado.short_description = 'Marcar seleccionados como revisados'

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('categoria', 'nombre', 'clave', 'descripcion', 'fecha_caducidad', 'cantidad', 'status', 'dias_para_caducar')
    search_fields = ('categoria', 'nombre', 'clave', 'descripcion', 'fecha_caducidad', 'cantidad', 'status')
    date_hierarchy = 'created'
    list_filter = ('categoria', 'nombre', 'status')
    ordering = ('nombre',)  # Ordenar por nombre por defecto
    actions = [export_as_csv, enviar_recordatorio_de_caducidad, marcar_como_revisado]

    def dias_para_caducar(self, obj):
        if obj.fecha_caducidad:
            dias_restantes = (obj.fecha_caducidad - datetime.now().date()).days
            return f'{dias_restantes} días'
        return 'No disponible'
    
    dias_para_caducar.short_description = 'Días para Caducidad'

    # Configuración de detalles del formulario
    fieldsets = (
        (None, {'fields': ('categoria', 'nombre', 'clave', 'descripcion', 'fecha_caducidad', 'cantidad', 'status')}),
        ('Fechas', {'fields': ('created', 'updated'), 'classes': ('collapse',)}),
    )

class AdministrarAsignacionSuministro(admin.ModelAdmin):
    list_display = ('asignado_a', 'medicamento', 'fecha_asignacion', 'cantidad', 'medicamento_detalle')
    search_fields = ('asignado_a', 'medicamento__nombre', 'fecha_asignacion')
    date_hierarchy = 'fecha_asignacion'
    list_filter = ('asignado_a', 'medicamento__nombre', 'fecha_asignacion')
    ordering = ('fecha_asignacion',)  # Ordenar por fecha de asignación por defecto

    def medicamento_detalle(self, obj):
        return format_html('<a href="{}">{}</a>', obj.medicamento.get_absolute_url(), obj.medicamento.nombre)

    medicamento_detalle.short_description = 'Detalle del Medicamento'

admin.site.register(Medicamento, AdministrarModelo)
admin.site.register(AsignacionSuministro, AdministrarAsignacionSuministro)
