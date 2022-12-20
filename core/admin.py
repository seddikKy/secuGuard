from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Entreprise)
admin.site.register(TagHeader)
admin.site.register(TagDetail)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_entreprise')
    ordering = ('name',)
    search_fields = ('name','id_entreprise',)

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_site')
    ordering = ('name',)
    search_fields = ('name','id_site',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_site')
    ordering = ('name',)
    search_fields = ('name','id_site',)