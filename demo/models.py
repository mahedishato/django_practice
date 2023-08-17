from django.db import models

# Create your models here.

class teaccher(models.Model):
    t_id = models.IntegerField()
    t_name = models.CharField(max_length=40)
    t_email = models.EmailField(max_length=30)

