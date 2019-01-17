from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	subject = models.CharField(max_length=20)
	message = models.TextField(blank=True, null=True)
	

	def __str__(self):
		return self.name