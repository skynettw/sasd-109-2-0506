from django.db import models
from django.utils import timezone

class MyList(models.Model):
	name = models.CharField(max_length=100)
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class TVList(models.Model):
	title = models.CharField(max_length=100)
	vid = models.CharField(max_length=20)
	mylist = models.ForeignKey(MyList, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

