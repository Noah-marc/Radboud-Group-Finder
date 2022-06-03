import datetime
from statistics import mode
from tokenize import group
from django.db import models
from multiselectfield import MultiSelectField

COURSE_CHOICES = (
    ("Calculus and Probability Theory", "Calculus and Probability Theory"),
    ("Hacking in C", "Hacking in C"),
)
STUDYPROGRAM_CHOICES = (
    ("Computing Science", "Computing Science"),
    ("Mathematics", "Mathematics"),
)
# Create your models here.
class Profile(models.Model):
    course = MultiSelectField(choices=COURSE_CHOICES, default="")
    firstName = models.TextField()
    lastName = models.TextField()
    studentNumber = models.TextField()
    studyProgram = models.CharField(max_length = 100, choices = STUDYPROGRAM_CHOICES, default = "")
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
    course = models.CharField(max_length=100, choices=COURSE_CHOICES, default= "")
    def __str__(self):
        return self.groupName

class Membership(models.Model): 
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.date.today)
    def __str__(self):
        return (self.group.__str__() + "-" + self.profile.__str__())