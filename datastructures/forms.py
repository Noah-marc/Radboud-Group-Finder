from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class ProfileForm(forms.Form):
    firstName = forms.CharField() 
    lastName = forms.CharField()
    studentNumber = forms.CharField()
    studyProgram = forms.CharField()
    age = forms.IntegerField() # make age input as only Natural Numbers!
    gender = forms.CharField()

class RegisterUserForm (UserCreationForm):
    id = forms.IntegerField()
    email = forms.EmailField
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    class Meta: 
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',  'password1' , 'password2')

class EditProfileForm (UserChangeForm): 



    #TO DO: Get Choice Filed for Gender working

    
    #GenderType = [
     #   "male", 
      #  "female", 
       # "other", 
    #]
    #gender = forms.ChoiceField()


    #!!!!!!!!!!!!!!!temporary function, replace by correct cleaning functions later on !!!!!!!!!!!!!!!!
    def clean_title(self): 
        cleaned_data = self.cleaned_data # this is a dictionary, containing cleaned data for all fileds in ProfileForm
        return cleaned_data


        
