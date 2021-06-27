from django.db import models


from django.contrib.auth.models import User



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, blank=True)
    country= models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.user.username

