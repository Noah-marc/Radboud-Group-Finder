import datetime
from pyexpat import model
from statistics import mode
from tokenize import group
from django.db import models
from django.contrib.auth.models  import User
from multiselectfield import MultiSelectField


COURSE_CHOICES = (
    ('Calculus and Probability Theory', 'Calculus and Probability Theory'),
    ('Hacking in C', 'Hacking in C'),
)

STUDYPROGRAM_CHOICES = (
    ("Computing Science", "Computing Science"),
    ("Mathematics", "Mathematics"),
)

GENDER_TYPES = (
    ("male", "male"), 
    ("female", "female"), 
    ("other", "other")
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE, default="")
    course = MultiSelectField(choices = COURSE_CHOICES, default="")
    firstName = models.TextField(default="")
    lastName = models.TextField(default="")
    studentNumber = models.TextField()
    studyProgram = MultiSelectField(choices = STUDYPROGRAM_CHOICES, default = "")
    age = models.PositiveIntegerField(null = True)
    class GenderType(models.TextChoices):
        MALE = "male", "male"
        FEMALE = "female", "female"
        OTHER= "other", "other"
    gender = models.CharField(max_length =10, choices = GenderType.choices, default = GenderType.MALE )
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.firstName

class Group(models.Model):
    groupName = models.CharField(max_length=100)
    groupSize = models.IntegerField(default=4)
    groupDescription = models.CharField(max_length=500, default = '')
    members = models.ManyToManyField(Profile, through='Membership', through_fields=('group', 'profile')) 
    course = models.CharField(max_length=100, choices=COURSE_CHOICES, default= "")
    def __str__(self):
        return self.groupName

class Membership(models.Model): 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    group_joined = models.BooleanField(default=False)
    isOwner = models.BooleanField(default=False)
    def __str__(self):
        return (self.group.__str__() + "-" + self.profile.__str__())
    def get_profile(self):
        return (self.profile.__str__())
    def get_group(self):
        return (self.group.__str__())