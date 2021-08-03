from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    desc = models.TextField(max_length=200)
    timestamp = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.name

