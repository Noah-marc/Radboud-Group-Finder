from django.db import models

# Create your models here.

class Groups(models.Model):
    groupName = models.TextField()
    groupSize = models.IntegerField()
    groupCourse = models.TextField()
