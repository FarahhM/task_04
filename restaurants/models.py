from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name= models.CharField(max_length=20)
	description=models.TextField()
	opening_time=models.DateTimeField(auto_now_add=True)
	closing_time=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
