from django.contrib import admin
from .models import Project


class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description')

admin.site.register(Project,ProjetAdmin)
