from django.contrib import admin
from .models import Converter
# Register your models here.

class ConverterAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    
    
    list_per_page = 20

admin.site.register(Converter, ConverterAdmin)