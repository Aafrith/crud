from django.db import models
from django.contrib.auth.models import User

# Employee model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link each employee to a user

    def __str__(self):
        return self.name
