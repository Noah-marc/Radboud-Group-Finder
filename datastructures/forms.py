from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile
from django.contrib.auth import get_user



class ProfileCreationForm(forms.ModelForm):
    # studentNumber = forms.CharField()
    # STUDYPROGRAM_CHOICES = (
    #     ("Computing Science", "Computing Science"),
    #     ("Mathematics", "Mathematics"),
    #     ("none", "none")
    # )
    # studyProgram = forms.MultipleChoiceField(choices = STUDYPROGRAM_CHOICES, 
    #                                          initial = "none", 
    #                                          required = True,
    #                                          label = "Study Program"                                   
    # )
    # age = forms.IntegerField() # make age input as only Natural Numbers!
    # gender = forms.CharField()
    class Meta: 
        model = Profile
        fields = ['studentNumber', 'studyProgram', 'age', 'gender']
    

class RegisterUserForm (UserCreationForm):
    email = forms.EmailField(required= True, label='')
    first_name = forms.CharField(max_length = 50, label='')
    last_name = forms.CharField(max_length = 50, label='')
    class Meta: 
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',  'password1' , 'password2')

class EditUserForm():
    username= forms.CharField(max_length = 50, required = True) 
    email = forms.EmailField(required = True, )
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField()

    class Meta: 
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class EditProfileForm (UserChangeForm): 
    student_number = forms.CharField()
    COURSE_CHOICES = (
        ("Calculus and Probability Theory", "Calculus and Probability Theory"),
        ("Hacking in C", "Hacking in C"), 
        ("none", "none")
    )
    courses = forms.MultipleChoiceField(choices = COURSE_CHOICES, 
                                        initial = "none",        
                                        required = True, 
                                        label= 'Courses'
                                        )
    STUDYPROGRAM_CHOICES = (
        ("Computing Science", "Computing Science"),
        ("Mathematics", "Mathematics"),
        ("none", "none")
    )
    studyProgram = forms.MultipleChoiceField(choices = STUDYPROGRAM_CHOICES, 
                                             initial = "none", 
                                             required = True,
                                             label = "Study Program"                                   
    )
    age = forms.IntegerField(required= True)
    # class Meta: 
    #     model = Profile
    #     fields = ('student_number', ')
                                        





    #TO DO: Get Choice Filed for Gender working

    
    #GenderType = [
     #   "male", 
      #  "female", 
       # "other", 
    #]
    #gender = forms.ChoiceField()


    #!!!!!!!!!!!!!!!temporary function, replace by correct cleaning functions later on !!!!!!!!!!!!!!!!
    # def clean_title(self): 
    #     cleaned_data = self.cleaned_data # this is a dictionary, containing cleaned data for all fileds in ProfileForm
    #     return cleaned_data


        
