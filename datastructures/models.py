import datetime
from tokenize import group
from django.db import models

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
    gender = models.CharField(max_length = 1, choices = GenderType.choices, default = GenderType.MALE)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.firstName

class Group(models.Model):
    groupName = models.CharField(max_length=100)
    groupSize = models.IntegerField(default=4)
    groupDescription = models.CharField(max_length=500, default = '')
    members = models.ManyToManyField(Profile, through='Membership', through_fields=('group', 'profile')) 
    class groupCourse(models.TextChoices):
        NONE = "", "None"
        CALCULUS = "CaPT", "Calculus"
        HACKING = "HiC", "Hacking in C"
    course = models.CharField(max_length=10, choices=groupCourse.choices, default= groupCourse.NONE)
    def __str__(self):
        return self.groupName

class Membership(models.Model): 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.date.today)
    def __str__(self):
        return (self.group.__str__() + "-" + self.profile.__str__())


# class Profile(models.Model):
#     firstName = models.CharField(max_length=50)
#     def __str__(self):
#         return self.firstName

# class Group(models.Model):
#     groupName = models.CharField(max_length=128)
#     members = models.ManyToManyField(
#         Profile,
#         through='Membership',
#     )
#     def __str__(self):
#         return self.groupName

# class Membership(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     def __str__(self):
#         return (self.group.__str__() + "-" + self.profile.__str__())