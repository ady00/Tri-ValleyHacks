from django.contrib import admin
from .models import Painting

class PaintingAdmin(admin.ModelAdmin):
    list_display = ("title", "time_period", "location", "artist")
    
admin.site.register(Painting, PaintingAdmin)