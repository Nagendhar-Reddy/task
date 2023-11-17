
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['name']
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']
        
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'description']
        
class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['date', 'status']
        
class YourModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = ['name', 'description', 'images']
        
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']
        


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['subject', 'message', 'recipient']
        

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['title', 'description', 'date', 'time']
        


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['content']
        
        
class SupportForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    question = forms.CharField(label='Your Question', widget=forms.Textarea)
    

class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TeacherRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass