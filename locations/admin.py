from django.contrib import admin
from .models import DailyCookies
# Register your models here.

@admin.register(DailyCookies)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'location','user']
