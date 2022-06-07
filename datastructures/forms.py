from msilib.schema import Class
from socket import fromshare
from unittest.util import _MAX_LENGTH
from django import forms
<<<<<<< HEAD
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm
=======
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

>>>>>>> eedf3fa972f58c7427e80b10dc0d63b6b660c365


class ProfileForm(forms.Form):
    firstName = forms.CharField() 
    lastName = forms.CharField()
    studentNumber = forms.CharField()
    studyProgram = forms.CharField()
    age = forms.IntegerField() # make age input as only Natural Numbers!
    gender = forms.CharField()

<<<<<<< HEAD

class RegisterUserForm (UserCreationForm):
=======
class RegisterUserForm (UserCreationForm):
    id = forms.IntegerField()
>>>>>>> eedf3fa972f58c7427e80b10dc0d63b6b660c365
    email = forms.EmailField
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    class Meta: 
        model = User
<<<<<<< HEAD
        fields = ('username' , 'first_name', 'last_name','email',  'password1' , 'password2')
=======
        fields = ('username', 'first_name', 'last_name', 'email',  'password1' , 'password2')

class EditProfileForm (UserChangeForm): 



    #TO DO: Get Choice Filed for Gender working
>>>>>>> eedf3fa972f58c7427e80b10dc0d63b6b660c365

    
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


        
