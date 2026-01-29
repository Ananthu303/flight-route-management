"""
App configuration for airports app.
"""

from django.apps import AppConfig


class AirportsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'airports'
    verbose_name = 'Airport Routes Management'
