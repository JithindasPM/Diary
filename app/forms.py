from app.models import User,Diary_Model
from django import forms

class Signin_Modelform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Password'}),
        }

class Login_Modelfrom(forms.Form):
    
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}))
    password=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Password'}))
    

class Diary_Modelform(forms.ModelForm):
    class Meta:
        model=Diary_Model
        fields=['title','note']
        widgets={
           'title':forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Title'}),
           'note':forms.Textarea(attrs={'class':'form-control my-2','placeholder':'Dear diary,'})
            }




