from django.db import models
from groups import models as groupsModels

# Create your models here.


class Profile(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    studentNumber = models.TextField()
    studyProgram = models.TextField()
    age = models.IntegerField()
    class GenderType(models.TextChoices): 
        MALE = "m", "male"
        FEMALE = "f", "female"
        OTHERS = "o", "other"
    gender = models.CharField(max_length = 1, choices = GenderType.choices, default = GenderType.MALE )
    groups = models.ManyToManyField(groupsModels.Groups, related_name="profiles")
    