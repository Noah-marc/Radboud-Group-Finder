from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    student_number = models.TextField()
