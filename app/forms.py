from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm,UsernameField,UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.fields import Field
from django.forms.models import ModelForm
from django.utils.translation import gettext,gettext_lazy as _
from app.models import Expense,TaskModel,ProfileModel
from django.core import validators
from django.core.exceptions import ValidationError
from app.models import UserLogin,UserCreation,GroupName

class GroundNameForm(ModelForm):
    class Meta:
        model=GroupName
        fields=['gname','groupname']


class UserLoginForm(ModelForm):
    class Meta:
        model=UserLogin
        fields=["ulname","ulpassword"]
        widgets={
            'ulname':forms.TextInput(attrs={"class":'form-control form-control-sm mb-3'}),
            'ulpassword':forms.PasswordInput(attrs={"class":'form-control form-control-sm mb-3'})
        }

# class UserCreationForm(forms.Form):
#     uname=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":'form-control form-control-sm mb-3'}))
#     pwd=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={"class":'form-control form-control-sm mb-3'}))
#     rpwd=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={"class":'form-control form-control-sm mb-3'}))

#     def clean(self):
#         cleaned_data=super().clean()
#         upwd=self.cleaned_data['pwd']
#         urpwd=self.cleaned_data['rpwd']
#         if upwd != urpwd:
#             raise forms.ValidationError("Password not matching")


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label_suffix="",
        widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control form-control-sm mb-3','placeholder':"Enter password"}))

    password = forms.CharField(
        label_suffix="",
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control form-control-sm mb-4','placeholder':"Enter password"}),
    )

class SignupForm(UserCreationForm):
    password1=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':"form-control mb-3"}))
    password2=forms.CharField(
        label="Conform Password",
        widget=forms.PasswordInput(attrs={'class':"form-control mb-3"}))
        
    class Meta:
        model=User
        fields=['username','first_name','email']
        labels={'email':"Email"}
        widgets={
            "first_name":forms.TextInput(attrs={"class":'form-control form-control-sm mb-3'}),
            'email':forms.EmailInput(attrs={"class":"form-control form-control-sm mb-3"}),
            'username':forms.TextInput(attrs={"class":"form-control form-control-sm mb-3"}),
        }



class DateInput(forms.DateInput):
    input_type = 'date'


class ExpenseForm(ModelForm):
    class Meta:
        model=Expense
        fields=['itemname','price','quantity','date']
        labels={'itemname':"Item Name",'pirce':'Price','quantity':"Qty",'data':"Date"}
        widgets={
            'itemname':forms.TextInput(attrs={"class":'form-control form-control-sm mb-3'}),
            'price':forms.NumberInput(attrs={"class":'form-control form-control-sm mb-3'}),
            'quantity':forms.TextInput(attrs={"class":'form-control form-control-sm mb-3'}),
            # 'date':forms.DateInput(attrs={"class":'form-control form-control-sm mb-3'}),
            'date':DateInput(attrs={"class":'form-control form-control-sm mb-3'})
            
        }


class PasswordChangeForm(PasswordChangeForm):
    field_order = ['old_password', 'new_password1', 'new_password2']
    old_password = forms.CharField(
    label=_("Old password"),
    strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, "class":'form-control form-control-sm mb-3'}),
    )

    new_password1 = forms.CharField(
    label=_("New password"),
    strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, "class":'form-control form-control-sm mb-3'}),
    )

    new_password2 = forms.CharField(
    label=_("Confirm password"),
    strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, "class":'form-control form-control-sm mb-3'}),
    )

class TaskForm(ModelForm):
    class Meta:
        model=TaskModel
        fields=['name','start','end','note']
        labels={'name':'Task Name','start':'Start Date','end':'End Date','note':"Note"}
        widgets={
            'name':forms.TextInput(attrs={"class":'form-control form-control-sm mb-3'}),
            'start':DateInput(attrs={"class":'form-control form-control-sm mb-3'}),
            'end':DateInput(attrs={"class":'form-control form-control-sm mb-3'}),
            'note':forms.TextInput(attrs={"class":'form-control form-control-sm mb-3'}),
        }


martial= (
    ("married","Married"),
    ("unmarried","Unmarried"),
)

class EditProfileForm(ModelForm):
    martial=forms.ChoiceField(choices=martial,label="Martial Status",widget=(forms.RadioSelect(attrs={"class":'mt-1'})))
    class Meta:
        model=ProfileModel
        fields=['img','desc','occupation','martial']
        labels={"desc":"description",'martial':"martial status"}
        widgets= {
            'img':forms.FileInput(attrs={"class":'mb-2'}),
            "desc":forms.Textarea(attrs={"class":'form-control form-control-sm mb-3', 'rows':4, 'cols':15}),
            "occupation":forms.TextInput(attrs={"class":'form-control form-control-sm mb-3'}),
            
        }

class MakeProfileForm(ModelForm):
    martial=forms.ChoiceField(choices=martial,label="Martial Status",widget=(forms.RadioSelect(attrs={"class":'mt-1'})))
    class Meta:
        model=ProfileModel
        fields=['img','desc','occupation','martial']
        labels={'img':"Choose Image for Profile ","desc":"description",'martial':"martial status"}
        widgets= {
            # 'img':forms.FileInput(attrs={"class":'mb-2'}),
            "desc":forms.Textarea(attrs={"class":'form-control form-control-sm mb-3', 'rows':4, 'cols':15}),
            "occupation":forms.TextInput(attrs={"class":'form-control form-control-sm mb-3'}),     
        }
