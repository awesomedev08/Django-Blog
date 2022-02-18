from django.apps import AppConfig
from django import template

register = template.Library()

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
