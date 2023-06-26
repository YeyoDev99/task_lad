from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Task
from django.contrib.admin.widgets import AdminSplitDateTime 



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email','username','avatar','password1', 'password2']


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'bio']


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created', 'updated', 'user', 'completion', 'delay', 'completed'] 

class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created', 'updated', 'user', 'delay', 'completed', 'completion'] 