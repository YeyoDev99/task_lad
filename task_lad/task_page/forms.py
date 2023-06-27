from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Task
from django.contrib.admin.widgets import AdminSplitDateTime 
from django import forms

help_text_password = '''

Your password can’t be too similar to your other personal information. 
Your password must contain at least 8 characters. 
Your password can’t be a commonly used password. 
Your password can’t be entirely numeric.

Password


'''


class UserRegisterForm(UserCreationForm):
    
    password1 = forms.CharField(
        label= "Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password','placeholder':'password', 'id': 'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'password'}),
    )

    class Meta:
        model = User
        fields = ['name', 'email','username','avatar','password1', 'password2']
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'write your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'write your email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'write your username'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),

        }

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'bio']
        widgets= {
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control dick', 'placeholder': 'write your name'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write about you'}),

        }   


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created', 'updated', 'user', 'completion', 'delay', 'completed'] 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'write the task title'}),
            
            'description': forms.Textarea(attrs={
                                                'class': 'form-control description-text',
                                                'placeholder': 'task description'   
                                                }),
            
            'deadline': forms.DateTimeInput(attrs={
                                            'class': 'form-control', 
                                            'type': "datetime-local"}),

        }

class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created', 'updated', 'user', 'delay', 'completed', 'completion'] 
        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'write the task title'}),
            
            'description': forms.Textarea(attrs={
                                                'class': 'form-control description-text',
                                                'placeholder': 'task description'   
                                                }),
            
            'deadline': forms.DateTimeInput(attrs={
                                            'class': 'form-control', 
                                            'type': "datetime-local"}),

        }   
