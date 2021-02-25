from django import forms
from Sistema.models import Notas,Estudiante,Administrador,Bimestre,Docente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EstudianteNotasForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields= "__all__"

class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields= "__all__"

class BimestreForm(forms.ModelForm):
    class Meta:
        model = Bimestre
        fields= "__all__"


class BimestreFormx(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_name2 = forms.CharField(label='Your name', max_length=100) 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email','password1','password2']


