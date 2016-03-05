from django.contrib import admin

# Register your models here.
from django.contrib import admin	
from bread.models import Bread

class BreadAdmin(admin.ModelAdmin):
	list_display = ['id', 'description', 'image_file', 'filtered_image_file']
	
admin.site.register(Bread)