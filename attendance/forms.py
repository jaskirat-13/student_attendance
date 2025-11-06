from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Attendance, Feedback

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ('username','email','role','password1','password2')

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('student','date','status')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('message',)
