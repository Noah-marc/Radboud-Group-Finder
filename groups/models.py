from cProfile import Profile
from statistics import mode
from django.db import models

# Create your models here.
# to update database:
# python manage.py makemigrations
# python manage.py migrate

class Groups(models.Model):
<<<<<<< HEAD
    groupName = models.TextField()
    groupSize = models.IntegerField()
    groupCourse = models.TextField()
=======
    groupName = models.CharField(max_length=100)
    class groupCourse(models.TextChoices):
        NONE = "", ""
        CALCULUS = "CaPt", "calculus and probability theory"
        HACKING = "HiC", "hacking in C"
    course = models.CharField(choices=groupCourse.choices, default= groupCourse.NONE)

  # groupMembers = models.ManyToManyField(Profile, through='Membership')


>>>>>>> fceb2096b542db63c2d0713637707dfb57161add
