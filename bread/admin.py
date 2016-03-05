from django.contrib import admin

# Register your models here.
from django.contrib import admin	
from bread.models import Bread

class BreadAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'release_at', 'created_at']

admin.site.register(Bread, BreadAdmin)