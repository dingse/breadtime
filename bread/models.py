from __future__ import unicode_literals

from django.db import models
import datetime

from django.utils import timezone

from django.core.urlresolvers import reverse_lazy

# Create your models here.
class Bread(models.Model):
	name = models.TextField(default='noname')
	image_file = models.ImageField(upload_to='original/%Y/%m/%d')
	filtered_image_file = models.ImageField(upload_to='filtered/%Y/%m/%d') 
		# Can be extended to a thumnail or an image chain
	release_at = models.DateTimeField(default = timezone.now)
	description = models.TextField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add = True)

	#def upload(self):
	#	self.save()

	def delete(self, *args, **kwargs):
		self.image_file.delete()
		self.filtered_image_file.delete()
		super(Bread, self).delete(*args, **kwargs)

	def get_absolute_url(self):
		return reverse_lazy('view_single_bread', kwargs={'bread_id': self.id})

class Bread_object(Bread):
	pass
