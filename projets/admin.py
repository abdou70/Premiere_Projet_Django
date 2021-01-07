from django.contrib import admin
from .models import Projets

# Register your models here.

class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre','description')


admin.site.register(Projets,ProjetAdmin)