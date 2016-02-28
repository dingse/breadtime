from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Photo(models.Model):
	image_file = models.ImageField()
	filtered_image_file = models.ImageField() 
		# Can be extended to a thumnail or an image chain
	description = models.TextField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add = True)
