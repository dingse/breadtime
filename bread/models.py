from __future__ import unicode_literals

from django.db import models
import datetime

from django.utils import timezone

# Create your models here.
class Bread(models.Model):
	name = models.TextField(default='noname')
	image_file = models.ImageField(upload_to='original/%Y/%m/%d')
	filtered_image_file = models.ImageField(upload_to='filtered/%Y/%m/%d') 
		# Can be extended to a thumnail or an image chain
	description = models.TextField(max_length = 1000)
	release_at = models.DateTimeField(default = timezone.now)
	created_at = models.DateTimeField(auto_now_add = True)

	#def upload(self):
	#	self.save()

	def delete(self, *args, **kwargs):
		self.image_file.delete()
		self.filtered_image_file.delete()
		super(Bread, self).delete(*args, **kwargs)

