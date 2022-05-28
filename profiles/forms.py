from socket import fromshare
from django import forms

class ProfileForm(forms.Form):
    firstName = forms.CharField() 
    lastName = forms.CharField()
    studentNumber = forms.CharField()
    studyProgram = forms.CharField()
    age = forms.IntegerField() # make age input as only Natural Numbers!
    gender = forms.CharField()

    #TO DO: Get Choice Filed for Gender working

    
    #GenderType = [
     #   "male", 
      #  "female", 
       # "other", 
    #]
    #gender = forms.ChoiceField()


    #!!!!!!!!!!!!!!!temporary function, replace by correct cleaning functions later on !!!!!!!!!!!!!!!!
    def clean(self): 
        cleaned_data = self.cleaned_data # this is a dictionary, containing cleaned data for all fileds in ProfileForm
        return cleaned_data


        
