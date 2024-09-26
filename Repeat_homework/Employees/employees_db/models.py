from django.db import models


class Employee(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.CharField(max_length=100, null=True)
  position = models.CharField(max_length=100, null=True)

  def __str__(self):
    return f"{self.firstname}"
