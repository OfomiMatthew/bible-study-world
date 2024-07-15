from django.forms import ModelForm 
from django import forms
from .models import Room, Message,User
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']


class RoomForm(ModelForm):
    
    class Meta:
        model = Room 
        fields = "__all__"
        exclude =['host','participants']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email','bio']
    

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user