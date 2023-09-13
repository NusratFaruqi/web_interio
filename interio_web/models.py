from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    massage = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.email
