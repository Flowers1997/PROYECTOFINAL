#Blog
from django import forms
from .models import Post, Avatar
from App1 import models
#USER SYSTEM
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User





class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'post_body', 'image_up')
   
#USER SYSTEM

class UserRegistrationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')
     
    
class UserEditForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    last_name= forms.CharField(label="Modificar Apellido")
    first_name= forms.CharField(label="Modificar Nombre")


    class Meta:
        model=User
        fields=('email', 'password1', 'password2', 'last_name', 'first_name')
        

#Avatar
class AvatarForm(forms.Form):
    avatar= forms.ImageField(label="Avatar")