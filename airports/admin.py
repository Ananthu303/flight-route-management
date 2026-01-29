"""
Admin configuration for Airport Routes System.
"""

from django.contrib import admin
from .models import AirportRoute


@admin.register(AirportRoute)
class AirportRouteAdmin(admin.ModelAdmin):
    """
    Admin interface for managing airport routes.
    """
    
    list_display = [
        'airport_code',
        'position',
        'duration',
        'left',
        'right',
        'created_at'
    ]
    
    list_filter = ['created_at', 'updated_at']
    
    search_fields = ['airport_code', 'position']
    
    fieldsets = (
        ('Airport Information', {
            'fields': ('airport_code', 'position', 'duration')
        }),
        ('Route Connections', {
            'fields': ('left', 'right'),
            'description': 'Connect this airport to other airports in the route network'
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    ordering = ['airport_code']
    
    def get_queryset(self, request):
        """Optimize queries by selecting related objects."""
        qs = super().get_queryset(request)
        return qs.select_related('left', 'right')
