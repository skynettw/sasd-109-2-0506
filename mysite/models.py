from django.db import models

class TVList(models.Model):
    title = models.CharField(max_length=100)
    vid = models.CharField(max_length=20)

    def __str__(self):
        return self.title